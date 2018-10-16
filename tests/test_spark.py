def test_spark_fixture(spark_df):
    assert 'col_a' in spark_df.columns
