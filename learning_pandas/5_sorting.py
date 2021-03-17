import pandas as pd
import random as rand
pd.set_option('display.max_columns', 200)
pd.set_option('display.min_rows', 60)
pd.set_option('display.width', 4000)

def create_nice_rand_df():
    columns = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    df = pd.DataFrame([[rand.randint(0, 99) for i in range(10)] for j in range(30)], columns=columns)
    df.loc[0:10, 'ten'] = 'London'
    df.loc[10:20, 'ten'] = 'Paris'
    df.loc[20:30, 'ten'] = 'Moscow'
    df.loc[:, 'nine'] = ['even' if x % 2 == 0 else 'odd' for x in range(30)]
    return df

# Create sample dataframe
df = create_nice_rand_df()

# ______________________________________________________________________________________________________________________
# Options for df.sort_values()
# inplace=True                  To sort df inplace
# ignore_index=True             To reset index after sorting
# ascending=True                To sort in asc / desc order
# ascending=[True, False, ...]  To specify sort order for each column we are sorting by (if 'by' parameter is also a list).

# ______________________________________________________________________________________________________________________
# Sort dataframe
df.sort_values(by='one')            # Sort by 1 column
df.sort_values(by=['ten', 'nine'])  # Sort by 2 or more columns

# Sort series
df['one'].sort_values()

# ______________________________________________________________________________________________________________________
# N largest values (in column)
df.sort_values('one', ascending=False).head(5)  # dataframe
df.nlargest(5, 'one')                           # dataframe     df.nlargest(n, 'col_name')
df['one'].nlargest(5)                           # series        series.nlargest(n)

# N smallest values (in column)
df.sort_values('one').head(5)   # dataframe
df.nsmallest(5, 'one')          # dataframe     df.smallest(n, 'col_name')
df['one'].nsmallest(5)          # series        series.smallest(n)

# ______________________________________________________________________________________________________________________



