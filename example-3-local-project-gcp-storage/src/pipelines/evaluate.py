import argparse
import joblib
import json
import mlflow
from mlflow import log_param, log_metric, log_artifact
from mlflow.sklearn import log_model
from mlflow.tracking import MlflowClient
from sklearn.metrics import confusion_matrix, f1_score
import os
from typing import Text
import yaml

from src.data.load import get_dataset
from src.utils import get_logger
from src.report.visualize import plot_confusion_matrix


def evaluate_model(config_path: Text):

    pipeline_config = yaml.load(open(config_path), Loader=yaml.FullLoader)
    config = pipeline_config.get('evaluate')

    logger = get_logger(name='EVALUATE MODEL', loglevel=pipeline_config.get('base').get('loglevel'))
    logger.debug(f'Start evaluation...')

    EXPERIMENT_NAME = pipeline_config['base']['experiments']['name']
    MLFLOW_TRACKING_URI = pipeline_config['base']['MLFLOW_TRACKING_URI']
    target_column = pipeline_config['dataset_build']['target_column']
    test_dataset = get_dataset(pipeline_config['split_train_test']['test_csv'])
    model_name = pipeline_config['base']['experiments']['model_name']
    models_folder = pipeline_config['base']['experiments']['models_folder']

    model = joblib.load(os.path.join(models_folder, model_name))
    logger.debug(f'Model {model}')

    # Get X and Y
    y_test = test_dataset.loc[:, target_column].values.astype("float32")
    X_test = test_dataset.drop(target_column, axis=1).values
    X_test = X_test.astype("float32")

    scores = model.predict(X_test)

    f1 = f1_score(y_true=y_test, y_pred=scores, average='macro')
    cm = confusion_matrix(scores, y_test)

    test_report = {
        'f1_score': f1,
        'confusion_matrix': cm.tolist()
    }
    test_report_filepath = os.path.join(pipeline_config['base']['experiments']['experiments_folder'],
                            config['metrics_report'])
    json.dump(obj=test_report, fp=open(test_report_filepath, 'w'), indent=2)
    logger.debug(f'Test report: {test_report}')

    species = test_dataset['species'].unique().tolist()
    plt = plot_confusion_matrix(cm, species, normalize=False)
    confusion_matrix_filepath = os.path.join(pipeline_config['base']['experiments']['experiments_folder'],
                            f'{EXPERIMENT_NAME}_confusion_matrix.svg')
    plt.savefig(confusion_matrix_filepath)

    # Set tracking URI

    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.tracking.get_tracking_uri()
    client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

    if client.get_experiment_by_name(EXPERIMENT_NAME):
        pass
    else:
        client.create_experiment(EXPERIMENT_NAME)

    experiment_id = client.get_experiment_by_name(EXPERIMENT_NAME).experiment_id


    with mlflow.start_run(experiment_id=experiment_id) as run:

        logger.debug(f'Start logging for Experiment run: {run}')
        logger.debug(run.info)
        logger.debug(run.info.run_uuid)

        log_param(key='estimator', value=pipeline_config['train']['estimator_name'])
        log_param(key='cv', value=pipeline_config['train']['cv'])

        log_metric(key='f1_score', value=f1)
        log_artifact(local_path=confusion_matrix_filepath)
        log_artifact(local_path=test_report_filepath)
        log_model(model, artifact_path=model_name)

    logger.debug(f'Metrics and artefacts logged to MLPanel')


if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    evaluate_model(config_path=args.config)
