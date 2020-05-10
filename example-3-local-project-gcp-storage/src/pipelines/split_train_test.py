import argparse
from typing import Text
import yaml

from src.data.load import get_dataset
from src.data.trainsforms import transform_targets_to_numerics, split_dataset_in_train_test
from src.utils import get_logger



def split_dataset(config_path: Text):

    pipeline_config = yaml.load(open(config_path), Loader=yaml.FullLoader)
    config = pipeline_config.get('split_train_test')


    logger = get_logger(name = 'SPLIT_TRAIN_TEST', loglevel=pipeline_config.get('base').get('loglevel'))
    logger.debug(f'Start split_dataset')

    dataset = get_dataset(pipeline_config['dataset_build']['dataset_csv'])
    target_column = pipeline_config['dataset_build']['target_column']
    random_state = pipeline_config['base']['random_state']

    test_size = config['test_size']
    train_csv_path = config['train_csv']
    test_csv_path = config['test_csv']
    logger.debug(f'Test size: {test_size}')

    dataset = transform_targets_to_numerics(dataset, target_column=target_column)
    train_dataset, test_dataset = split_dataset_in_train_test(dataset, test_size=test_size, random_state=random_state)

    train_dataset.to_csv(train_csv_path, index=False)
    test_dataset.to_csv(test_csv_path, index=False)

    logger.debug(f'Train dataset shape: {train_dataset.shape}')
    logger.debug(f'Save train dataset to {train_csv_path}')
    logger.debug(f'Test dataset shape: {test_dataset.shape}')
    logger.debug(f'Save test dataset to {test_csv_path}')



if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    split_dataset(config_path=args.config)

