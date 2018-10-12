import pandas as pd
import pytest


@pytest.fixture()
def df():
    return pd.DataFrame({
        'col_a': ['a', 'a', 'a'],
        'col_b': ['b', 'b', 'b'],
        'col_c': ['c', 'c', 'c'],
    })


@pytest.fixture()
def df_with_col_d():
    return pd.DataFrame({
        'col_a': ['a', 'a', 'a'],
        'col_b': ['b', 'b', 'b'],
        'col_c': ['c', 'c', 'c'],
        'col_d': ['d', 'd', 'd'],
    })


@pytest.fixture()
def db_creds():
    return {
        'host': 'fake_host',
        'dbname': 'fake_db',
        'user': 'fake_user',
        'password': 'fake_password'
    }
