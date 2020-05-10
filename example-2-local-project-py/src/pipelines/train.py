import argparse
from typing import Text

import joblib
import os
import yaml

from src.data.load import get_dataset
from src.train.train import train
from src.utils import get_logger


def train_model(config_path: Text):

    pipeline_config = yaml.load(open(config_path), Loader=yaml.FullLoader)
    config = pipeline_config.get('train')

    logger = get_logger(name='TRAIN MODEL', loglevel=pipeline_config.get('base').get('loglevel'))
    logger.debug(f'Start training...')

    estimator_name = config['estimator_name']
    param_grid = config['estimators'][estimator_name]['param_grid']
    cv = config['cv']

    target_column = pipeline_config['dataset_build']['target_column']
    train_df = get_dataset(pipeline_config['split_train_test']['train_csv'])

    model = train(
        df=train_df,
        target_column=target_column,
        estimator_name=estimator_name,
        param_grid=param_grid,
        cv=cv
    )
    logger.debug(f'Best score: {model.best_score_}')

    model_name = pipeline_config['base']['experiments']['model_name']
    models_folder = pipeline_config['base']['experiments']['models_folder']

    joblib.dump(
        model,
        os.path.join(models_folder, model_name)
    )
    logger.debug(f'Save model to {os.path.join(models_folder, model_name)}')


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    train_model(config_path=args.config)

