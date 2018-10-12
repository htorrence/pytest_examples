import pandas as pd
import pytest

from pytest_examples.functions_to_test import add_col


@pytest.mark.usefixtures('df')
@pytest.mark.usefixtures('df_with_col_d')
def test_add_col_passes(df, df_with_col_d):
    actual = add_col(df, 'col_d', 'd')
    expected = df_with_col_d

    pd.testing.assert_frame_equal(actual, expected)


@pytest.mark.usefixtures('df_with_col_d')
def test_add_col_exception(df_with_col_d):
    with pytest.raises(ValueError) as err:
        add_col(df_with_col_d, 'col_d', 'd')

    assert str(err.value) == 'column already exists'
