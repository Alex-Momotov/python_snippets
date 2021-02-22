import pandas as pd
from random import randint
pd.set_option('display.max_columns', 200)
pd.set_option('display.min_rows', 60)
pd.set_option('display.width', 4000)

# Create sample dataframe
columns = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
df = pd.DataFrame([[randint(0, 1) for i in range(10)] for j in range(30)], columns=columns)

# ______________________________________________________________________________________________________________________
# Rename columns
df.rename(columns={'one': 'FIRST', 'ten': 'LAST'}, inplace=True)    # Specific columns
df.columns = [x.upper() for x in df.columns]                        # All columns - make upper case
df.columns = [x.replace(' ', '_') for x in df.columns]              # All columns - replace ' ' with '_'

# ______________________________________________________________________________________________________________________
# Change values - iloc
df.iloc[0, 0] = 'hello'     # one value
df.iloc[:, 2] = 'cat'       # column
df.iloc[:, [0, 2]] = 'bar'  # columns
df.iloc[2, :] = 'dog'       # row
df.iloc[[0, 2], :] = 'foo'  # rows
df.iloc[2:8, 2:8] = 'fox'   # df selection
df.iloc[:, :] = 1           # df

# Change values - loc
df.loc[0, 'one'] = 'hello'           # one value
df.loc[:, 'two'] = 'cat'             # column
df.loc[:, ['one', 'three']] = 'bar'  # columns
df.loc[2, :] = 'dog'                 # row
df.loc[[0, 2], :] = 'foo'            # rows
df.loc[5:9, 'three':'seven'] = 'fox' # df selection
df.loc[:, :] = 1                     # df

# Change values - by filter
filt = df['one'] > 0
df.loc[filt, 'one'] = 'big'

df.loc[:, :] > 0

# ______________________________________________________________________________________________________________________
# Change entire column

# Using list comprehensions
df['city'] = [x.upper() for x in df['city']]

# Using pandas StringMethods
df['city'] = df.City.str.upper()

# ______________________________________________________________________________________________________________________
# Adding new collumns

# New arbitrary column
df['zeros'] = [0 for i in df.City]

# Using list comprehensions on existing columns
df['city_upper'] = [x.upper() for x in df.City]
df['city_lower'] = [x.lower() for x in df.City]

# As operation between two existing columns
df


# ______________________________________________________________________________________________________________________
# Series.apply(func)        # return copy of series with func applied
# Series.replace({'old_val': 'new_val'})      # map one or more values to another
# DataFrame.apply(func)     # Apply func to each series of dataframe. Pass asix='columns' to apply along rows
# DataFrame.applymap(func)  # Apply func to each element in dataframe.

