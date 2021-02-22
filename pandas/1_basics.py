import pandas as pd
from random import randint

# ______________________________________________________________________________________________________________________
# Options for printing dataframe
pd.set_option('display.max_columns', 200)   # Max columns to display
pd.set_option('display.min_rows', 60)       # Num rows to display in truncated view
pd.set_option('display.width', 4000)        # Avoid wrapping (if no Jupyter notebook)

#_______________________________________________________________________________________________________________________
# Read CSV as dataframe
# First included row should be headers.
df = pd.read_csv('pandas/data/olympics.csv', skiprows=4)
                                # skiprows=x        Skip first x lines of CSV (often meaningless data).
                                # index_col='col1'  Set column as dataframe index.

# ______________________________________________________________________________________________________________________
# Create sample dataframe
columns = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
df = pd.DataFrame([[randint(0, 1) for i in range(10)] for j in range(30)], columns=columns)

# ______________________________________________________________________________________________________________________
# Explore dataframe
df          # First and last 5 rows
df.shape    # Tuple (rows, columns)
df.head(2)  # First x rows
df.tail(5)  # Last x rows

df.columns  # List of columns (Index type)
df.index    # Current index of dataframe (row numbers unless set otherwise)

# Explore type, and missing data
df.info()   # Num of non-null values per column, data type of each column
            # 'object' type usually means String.

# ______________________________________________________________________________________________________________________
# Slicing dataframe
# When indexing result is single value, the type is that column's type. df.loc[0, 'col1']       df.iloc[0, 0]     df['col1'][0]
# When indexing result is 1-dimensional structure, its a Series.        df['col_1']             df.loc[0]         df.iloc[0]
# When indexing result is 2-dimensional structure, its a DataFrame.     df[['col1', 'col2']]    df.loc[[0, 1]]    df.iloc[[0, 1], ['col1', 'col2']]
# Results are copy respective df or series, not a view, so no concern for aliases.

# Access columns
df.City                 # Single column by name. Only works if no space in series name, and no colision with method name.
df['Edition']           # Single column by name.
df[['City', 'Medal']]   # Multiple columns.

# df.iloc[rows, cols]   Access rows and columns by integer location
#                       <rows> and <cols> can be single number, list of numbers, slice of numbers (last exclusive).
df.iloc[0]                  # Single row.
df.iloc[[1, 2]]             # Multiple rows.
df.iloc[2, 3]               # Simgle row, single column.
df.iloc[[0, 1, 2], [0, 1]]  # Multiple rows, multiple columns.
df.iloc[0:2]                # Slice of rows (last excl).
df.iloc[5:10, 5:10]         # Slice of rows and columns (last excl).


# df.loc[rows, cols]    Access rows by index, columns by name
#                       <rows> can be single number, list of numbers, slice of numbers (last inclusive), boolean array.
#                       <columns> can be single string, list of strings, slice of strings (last inclusive), boolean array.
df.loc[0]                  # Single row.
df.loc[[1, 2]]             # Multiple rows.
df.loc[2, 'Medal']         # Simgle row, single column.
df.loc[[0, 1, 2], ['City', 'Medal']]  # Multiple rows, multiple columns.
df.loc[0:2]                 # Slice of rows (last incl)
df.loc[0:2, 'City':'Sport'] # Slice of rows and columns (last incl).

# ______________________________________________________________________________________________________________________
# Slicing series

first_row = df.iloc[0]
city_col = df.iloc['City']

# If series object was obtained from df row, values can be accessed by column name, by integer, by integer slice.
first_row['City']
first_row[0]
first_row[:5]

# If series object was obtained from df column, values can be accessed by dataframe index (row number by default).
city_col[0]
city_col[0:10]

# ______________________________________________________________________________________________________________________
# Dataframe index

# Behaviour with df.loc  and  df.iloc
# Index of a df is what is used as <rows> in df.loc[rows, cols]. By default its numbers range, but we can change it to be a df column.
# Setting index only affects df.loc behaviour, df.iloc still works as before.

# Uniqueness
# Index column doesn't have to have unique values. If values unique df.loc will return Series. If not unique df.loc will return dataframe.
# Usually though we want to set index using a column that has unique value for each record.

df.set_index('Edition')     # Returns df copy indexed by 'Edition' column (year).       Pass inplace=True to index inplace.
df.reset_index()            # Returns df copy indexed by the default number range.      Pass inplace=True to reset index inplace.
df.sort_index()             # Returns df copy with records sorted by index.             Pass inplace=True to sort index inplace.
                            #                                                           Pass ascending=False to sort index in descending order.

# Example
df_by_year = df.set_index('Edition')    # Index df by year
df_by_year.loc['2008']                  # Get values where Edition (year) is 2008
df_by_year.iloc[0]                      # We can still index by row numbers using df.iloc

# ______________________________________________________________________________________________________________________

