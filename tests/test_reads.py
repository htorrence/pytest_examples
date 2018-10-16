import pandas as pd
from unittest import mock

from pytest_examples.functions_to_test import (
    df_from_csv,
    string_from_file,
    psycopg_cursor_one_call,
    psycopg_cursor_two_calls,
)


@mock.patch('pytest_examples.functions_to_test.function_1')
@mock.patch('pytest_examples.functions_to_test.function_2')
@mock.patch('pytest_examples.functions_to_test.function_3')
def test_multiple_mocks(function_3_mock, function_2_mock, function_1_mock, df):
    pass


@mock.patch('pytest_examples.functions_to_test.pd.read_csv')
def test_df_from_csv_mock_function(read_csv_mock, df):
    # setup
    read_csv_mock.return_value = df

    # call function
    actual = df_from_csv('fake_file_name.csv')

    # set expectations
    expected = df

    # assertions
    pd.testing.assert_frame_equal(actual, expected)


@mock.patch.object(pd, 'read_csv')
def test_df_from_csv_mock_method(read_csv_mock, df):
    # setup
    read_csv_mock.return_value = df

    # call function
    actual = df_from_csv('fake_file_name.csv')

    # set expectations
    expected = df

    # assertions
    pd.testing.assert_frame_equal(actual, expected)


def test_string_from_file():
    with mock.patch('builtins.open', mock.mock_open(read_data='fake_file_contents')):
        actual = string_from_file('fake_file_name.csv')

    expected = 'fake_file_contents'
    assert actual == expected


def test_psychopg_cursor_one_call(db_creds):
    with mock.patch('psycopg2.connect') as mock_connect:
        psycopg_cursor_one_call(db_creds, 'fake_table')

    mock_connect().cursor().__enter__().execute.assert_called_with(
        'SELECT * FROM fake_table LIMIT 10;'
    )


def test_psychopg_cursor_two_calls(db_creds):
    with mock.patch('psycopg2.connect') as mock_connect:
        psycopg_cursor_two_calls(db_creds, 'fake_table')

    mock_connect().cursor().__enter__().execute.assert_has_calls([
        mock.call('SELECT * FROM fake_table LIMIT 10;'),
        mock.call('SELECT count(*) FROM fake_table;'),
    ])
