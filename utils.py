import os

import pandas as pd
import numpy as np


OP_SETTING_COLUMNS = ['op_setting_{}'.format(x) for x in range(1, 4)]
SENSOR_COLUMNS = ['sensor_{}'.format(x) for x in range(1, 22)]

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, 'CMAPSSData')


def read_data(filepath):
    '''
    Reads `filepath` as space separated file and returns pd.DataFrame
    '''
    col_names = ['unit', 'time_cycles'] + OP_SETTING_COLUMNS + SENSOR_COLUMNS
    return pd.read_csv(
        filepath,
        sep='\s+',
        header=None,
        names=col_names
    )

def read_dataset(dataset_name):
    '''
    Reads TRAIN, TEST and RUL datasets for specified dataset name

    Parameters
    ----------
    dataset_name : str, name of the dataset, e.g. 'FD001'

    Returns
    -------
    a tuple of (pd.DataFrame, pd.DataFrame, np.array) for TRAIN, TEST AND RUL
    datasets correspondingly
    '''
    TRAIN_FILE = os.path.join(DATA_DIR, f'train_{dataset_name}.txt')
    TEST_FILE = os.path.join(DATA_DIR, f'test_{dataset_name}.txt')
    TEST_RUL_FILE = os.path.join(DATA_DIR, f'RUL_{dataset_name}.txt')

    train_data = read_data(TRAIN_FILE)
    test_data = read_data(TEST_FILE)
    test_rul = np.loadtxt(TEST_RUL_FILE)

    return train_data, test_data, test_rul


def calculate_RUL(X, upper_threshold=None):
    '''
    Calculate Remaining Useful Life per `unit`

    Parameters
    ----------
    X : pd.DataFrame, with `unit` and `time_cycles` columns
    upper_threshold: int, limit maximum RUL valus, default is None

    Returns
    -------
    np.array with Remaining Useful Life values
    '''
    lifetime = X.groupby(['unit'])['time_cycles'].transform(max)
    rul = lifetime - X['time_cycles']

    if upper_threshold:
        rul = np.where(rul > upper_threshold, upper_threshold, rul)

    return rul
