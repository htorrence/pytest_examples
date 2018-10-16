import pandas as pd
import pytest

from pytest_examples.functions_to_test import add_col


def test_add_col_passes():
    # setup
    df = pd.DataFrame({
        'col_a': ['a', 'a', 'a'],
        'col_b': ['b', 'b', 'b'],
        'col_c': ['c', 'c', 'c'],
    })

    # call function
    actual = add_col(df, 'col_d', 'd')

    # set expectations
    expected = pd.DataFrame({
        'col_a': ['a', 'a', 'a'],
        'col_b': ['b', 'b', 'b'],
        'col_c': ['c', 'c', 'c'],
        'col_d': ['d', 'd', 'd'],
    })

    # assertion
    pd.testing.assert_frame_equal(actual, expected)


def test_add_col_passes_with_fixtures(df, df_with_col_d):
    actual = add_col(df, 'col_d', 'd')
    expected = df_with_col_d

    pd.testing.assert_frame_equal(actual, expected)


def test_add_col_exception(df_with_col_d):
    with pytest.raises(ValueError) as err:
        add_col(df_with_col_d, 'col_d', 'd')

    assert str(err.value) == 'column already exists'
