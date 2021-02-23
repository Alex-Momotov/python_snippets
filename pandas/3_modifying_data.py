import pandas as pd
import random as rand
pd.set_option('display.max_columns', 200)
pd.set_option('display.min_rows', 60)
pd.set_option('display.width', 4000)

def create_nice_rand_df():
    columns = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    df = pd.DataFrame([[rand.randint(0, 9) for i in range(10)] for j in range(30)], columns=columns)
    df.loc[0:10, 'ten'] = 'London'
    df.loc[10:20, 'ten'] = 'Paris'
    df.loc[20:30, 'ten'] = 'Moscow'
    df.loc[:, 'nine'] = ['even' if x % 2 == 0 else 'odd' for x in range(30)]
    return df

# Create sample dataframe
df = create_nice_rand_df()

# ______________________________________________________________________________________________________________________
# Replace value in dataframe
df.replace(1, 'one')             # Replace values in entire df.        Pass inplace=True.
df.replace({2:'two', 3:'hello'}) # Replace many values in entire df.   Pass inplace=True.

# Replace value in series
df.loc[0].replace(1, 'one')             # Replace values in entire df.        To persist change:  df.loc[0] = df.loc[0].replace(..)
df.loc[0].replace({2:'two', 3:'hello'}) # Replace many values in entire df.   To persist change:  df.loc[0] = df.loc[0].replace(..)

# ______________________________________________________________________________________________________________________
# Apply functions
df['one'].apply(func)             # Apply func to each value in series.
df.apply(func)                    # Apply func to each series of dataframe. Pass asix='columns' to apply along rows
df.applymap(func)                 # Apply func to each element in dataframe.

# ______________________________________________________________________________________________________________________
# Rename columns
df.rename(columns={'one': 'FIRST', 'ten': 'LAST'}, inplace=True)    # Specific columns
df.columns = [x.upper() for x in df.columns]                        # All columns - make upper case
df.columns = [x.replace(' ', '_') for x in df.columns]              # All columns - replace ' ' with '_'

# ______________________________________________________________________________________________________________________
# Set value - iloc
df.iloc[0, 0] = 'hello'     # one value
df.iloc[:, 2] = 'cat'       # column
df.iloc[:, [0, 2]] = 'bar'  # columns
df.iloc[2, :] = 'dog'       # row
df.iloc[[0, 2], :] = 'foo'  # rows
df.iloc[2:8, 2:8] = 'fox'   # df selection
df.iloc[:, :] = 1           # df

# Set value - loc
df.loc[0, 'one'] = 'hello'           # one value
df.loc[:, 'two'] = 'cat'             # column
df.loc[:, ['one', 'three']] = 'bar'  # columns
df.loc[2, :] = 'dog'                 # row
df.loc[[0, 2], :] = 'foo'            # rows
df.loc[5:9, 'three':'seven'] = 'fox' # df selection
df.loc[:, :] = 1                     # df

# Set value - by filter
filt = df['one'] > 0
df.loc[filt, 'one'] = 'big'

df.loc[:, :] > 0

# ______________________________________________________________________________________________________________________
# Modify values - number operation
df['one'] = df['one'] + 99
df['one'] = df['one'] / 2
df['one'] = df['one'] * 3 - 100

# Modify values - panda string methods
df['ten'] = df['ten'].str.upper()

# Modify values - as result between other columns
df['three'] = df.one + df.two

# Modify values - list comprehensions
df['one'] = [x + 5 for x in df['one']]

# Modify values - lambda
df['ten'] = df['ten'].apply(lambda x : x.lower())

# Modify values - function
def func(string):
    return string.upper()[:3]
df['ten'] = df['ten'].apply(func)

# ______________________________________________________________________________________________________________________
# Add column - arbitrary value
df['zeros'] = 0             # add 1 column
df[['new_1', 'new_2']] = 0  # add 2 columns

# Add column - all methods for moditying column values also work for adding new columns
df['new_col'] = df['ten'].apply(lambda x : x.lower())

# Add column - as long as result is a dataframe with expected num of new columns, we can create new columns this way
df[['new_1', 'new_2']] = df['ten'].str.split('nd', expand=True)   # Expand ensures df is returned

# ______________________________________________________________________________________________________________________
# Add rows
# ignore_index=True     Pass when adding rows or df with pre-existing index, to avoid messing up the index.
# df = df.append(...)   There is no inplace=True option, so we need to set df equal to the result of append().
df.append(df.loc[0])                # Append row
df.append(df.loc[0:5])              # Append dataframe (from selection)
df.append(df[df.ten == 'Paris'])    # Append dataframe (from filter)

# ______________________________________________________________________________________________________________________
# Delete column
df.drop(columns=['three', 'four'], inplace=True)

# Delete row
df.drop(index=0, inplace=True)  # Delete row with specified index
                                # We might want to reset index after deleting rows

# ______________________________________________________________________________________________________________________






