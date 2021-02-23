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
# # Filter - numbers
df.one == 5          # equal
df.one != 5          # unqeual
df.one < 5           # smaller
df.one > 5           # bigger
df.one >= 5          # bigger or equal

# Filter - strings                 All python string operators are valid
df.ten.str.contains('Lon')       # contains
df.ten.str.startswith('Lon')     # starts with
df.ten.str.endswith('don')       # ends with
df.ten.str.count('n') == 2       # specific character count
df.ten.str.len() == 5            # string length

# Filter - in operator
df.one.isin([1, 2, 3])               # in
df.ten.isin(['London', 'Paris'])     # in

# Filter - composite filters
(df.one > 5) & (df.ten == 'London')    # AND
(df.one > 5) | (df.ten == 'London')    # OR

# Filter - result between two columns
(df.one + df.two) > 10

# Filter - list comprehension
['lon' in city.lower() for city in df.ten]

# Filter - lambda
df.ten.apply(lambda city : city.startswith('Lon'))

# Filter - function
def is_london(string):
    return string.lower() == 'london'
df.ten.apply(is_london)

# ______________________________________________________________________________________________________________________
# Applying filters - Filter out rows, using column of bool values
df[df.ten == 'London']

# Applying filters - Filter out columns, using row of bool values
df.loc[:, [type(x) is not str for x in df.loc[0]]]

# ______________________________________________________________________________________________________________________
