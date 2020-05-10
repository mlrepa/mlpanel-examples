import argparse
import logging
from typing import Text
import yaml

from src.data.load import get_dataset
from src.data.features import extract_features
from src.utils import get_logger


def dataset_build(config_path: Text):


    pipeline_config = yaml.load(open(config_path), Loader=yaml.FullLoader)
    config = pipeline_config.get('dataset_build')

    logger = get_logger(name = 'BUILD_DATASET', loglevel=pipeline_config.get('base').get('loglevel'))
    logger.debug(f'Prepare dataset')

    dataset = get_dataset(config['dataset_csv'])

    logger.debug(f'Extracting features')
    featured_dataset = extract_features(dataset)

    filepath = config['featured_dataset_csv']
    featured_dataset.to_csv(filepath, index=False)
    logger.debug(f'Dataset saved to {filepath}')


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    dataset_build(config_path=args.config)