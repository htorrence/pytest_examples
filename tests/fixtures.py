import pandas as pd
import pytest
from pyspark.sql import SparkSession


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
def numeric_df():
    return pd.DataFrame({
        'col_1': [.1, .2, .3, .4],
        'col_2': [.1, .2, .3, .4],
        'col_3': [.1, .2, .3, .4],
    })


@pytest.fixture()
def db_creds():
    return {
        'host': 'fake_host',
        'dbname': 'fake_db',
        'user': 'fake_user',
        'password': 'fake_password',
    }


@pytest.fixture(scope='session')
def spark(request):
    """
    Creates a spark context

    Parameters
    ----------
    request: pytest.FixtureRequest object
        provides access to testing context
    """

    spark = (
        SparkSession
        .builder
        .appName('pytest-pyspark-local-testing')
        .master('local[2]')
        .getOrCreate()
    )

    request.addfinalizer(lambda: spark.stop())

    return spark


@pytest.fixture()
def spark_df(spark):
    return spark.createDataFrame(
        [
            ('a', 'b', 'c', 'd'),
            ('a', 'b', 'c', 'd')
        ],
        ['col_a', 'col_b', 'col_c', 'col_d']
    )
