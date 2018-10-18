"""
This file contains a set of functions to demonstrate different actions
a data scientist might take.
"""
import datadog
import pandas as pd
import psycopg2


def add_col(df, new_col_name, default_value):
    """Add a new column to the given dataframe with a default value"""
    if new_col_name in df.columns:
        raise ValueError('column already exists')

    df[new_col_name] = default_value

    return df


def df_from_csv(filename):
    """Return a dataframe read from a csv"""
    return pd.read_csv(filename)


def string_from_file(filename):
    """Return the contents of file as a string"""
    with open(filename) as f:
        file_contents = f.read()
    return file_contents


def psycopg_cursor_one_call(db_creds, table_name):
    connection = psycopg2.connect(**db_creds)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM {} LIMIT 10;'.format(table_name))


def psycopg_cursor_two_calls(db_creds, table_name):
    connection = psycopg2.connect(**db_creds)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM {} LIMIT 10;'.format(table_name))
        cursor.execute('SELECT count(*) FROM {};'.format(table_name))


def function_1():
    print('Inside function 1')


def function_2():
    print('Inside function 2')


def function_3():
    print('Inside function 3')


def initialize_datadog_wrong_args():
    # these are the wrong argument names! sadly not caught by spec...
    datadog.initialize(key='fake_api_key', host='fake_host')


def initialize_datadog_wrong_call():
    # these are the wrong argument names!
    datadog.init(api_key='fake_api_key', app_key='fake_app_key', host_name='fake_host')


def initialize_datadog():
    # these are the correct argument names
    datadog.initialize(api_key='fake_api_key', app_key='fake_app_key', host_name='fake_host')
