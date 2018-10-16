def test_spark_fixture(spark):
    spark.createDataFrame(
        [
            ('a', 'b', 'c', 'd'),
            ('a', 'b', 'c', 'd')
        ],
        ['col_a', 'col_b', 'col_c', 'col_d']
    )
