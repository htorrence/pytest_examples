"""
This file contains a set of functions to demonstrate different actions
a data scientist might take.
"""
import pandas as pd
import psycopg2


def add_col(df, new_col_name, default_value):
    """Add a new column with a default value"""
    
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


def generate_features(db_creds):
    
    #  ... some setup code ...
    
    eng = sqlalchemy.create_engine('fake_connection_string')
    df = pd.read_sql('SELECT col1, col2 FROM data_table;',con=eng)

    #  ... processing on df ...
                       
    return features
    
    
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
