'''
This module is developed to compare values in a single dataframe.
The dataframe is imported from providing a url.
columns is defined below in the function.
'''

import pandas as pd

# make a python function that reads url
def test_dataframe(Url, Columns):
    '''two inputs are needed in this module: url and column names
       the one I used for testing is url =
       "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"'''
    Url = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
    Columns = ['chicken', 'beef', 'sausage', 'bacon']
    dataframe = pd.read_csv(Url)
    print("the data file is imported")
    if set(list(dataframe.columns.values))&set(Columns) == set(list(dataframe.columns.values)):
        print('the column names match!')
    else:
        print('the column names do not match!')
    if len(dataframe.index) >= 1:
        print("there are at least 1 row in the dataframe")
    if len(set(dataframe.dtypes)) >= 2:
        print("there are more than one data type in the columns")
        # Now iterate over valus in each column to see if each data entry is the same
        for col in list(dataframe.columns):
            for a, b in zip(dataframe[col], dataframe[col]):
                if a != b:
                    print("some values in the same column are NOT equal")
        missing_val = dataframe.isnull().sum()
        for val in missing_val:
            if val != 0:
                print("there are missing values in", val, "column(s)")
            else:
                print("there are no missing values in the current column")
