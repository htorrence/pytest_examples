from pytest_examples.functions_to_test import function_1


def test_spark_fixture(spark_df):
    assert 'col_a' in spark_df.columns


def test_function_1(capsys):
    function_1()
    out, err = capsys.readouterr()
    assert out == 'Inside function 1\n'
