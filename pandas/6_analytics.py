import pandas as pd
import random as rand
import matplotlib.pyplot as plt

# Will display diagram each time plt function is called. Alternative is to call plt.show() each time manually.
plt.interactive(True)

pd.set_option('display.max_columns', 200)
pd.set_option('display.min_rows', 60)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 4000)

def create_nice_rand_df():
    columns = ['city', 'gender', 'salary', 'age', 'fav_num', 'six', 'seven', 'eight', 'nine', 'ten']
    df = pd.DataFrame([[rand.randint(0, 99) for i in range(10)] for j in range(30)], columns=columns)
    df.loc[0:10, 'city'] = 'London'
    df.loc[10:20, 'city'] = 'Paris'
    df.loc[20:30, 'city'] = 'Moscow'
    df.loc[:, 'gender'] = ['male' if x % 2 == 0 else 'female' for x in range(df.shape[0])]
    df['salary'] = [rand.randint(20, 70) * 1000 for i in range(df.shape[0])]
    df['age'] = [rand.randint(20, 45) for i in range(df.shape[0])]
    return df

# Create sample dataframe
df = create_nice_rand_df()

# ______________________________________________________________________________________________________________________
# Basic analytics - on series
df['salary'].sum()
df['salary'].min()
df['salary'].max()
df['salary'].median()
df['salary'].mean()
df['salary'].std()

# Basic analytics - on dataframe    (calculates analytics function for each column)
df.min()
df.max()
df.median()
df.mean()
df.std()

# ______________________________________________________________________________________________________________________
# df.describe()
# Shows basic statistics for each df column: count (number of non-NaN rows), mean, std, min, 25%, 50%, 75%, max.
df.describe()           # describe dataframe
df['city'].describe()    # describe series

# ______________________________________________________________________________________________________________________
# Count of unique values in series
# Pass dropna=False to include NaN or None values in value counts.
df['city'].value_counts()                    # Count unique values
df['city'].value_counts(normalize=True)      # Percentage unique values

# ______________________________________________________________________________________________________________________
# df.isnull().sum()
# Quick trick to count number of missing values per column. Missing values are None or NaN.
df.isnull().sum()

# ______________________________________________________________________________________________________________________
# Group by
# df.groupby(['col', 'col1']) returns GroupBy object, that can be used later.
gr_city = df.groupby(['city'])       # group results by column(s)

# Get group
gr_city.get_group('Moscow')          # df subset where group is specific value

# Aggregate
# General syntax: group_object['col_to_aggregate'].agg_function()
gr_city['salary'].sum()              #
gr_city['salary'].min()              #
gr_city['salary'].max()              #
gr_city['salary'].median()           #
gr_city['salary'].mean()             #
gr_city['salary'].std()              #

gr_city['salary'].nlargest(3)        # N largest values from each group    (3 largest salaries from each city)
gr_city['salary'].nsmallest(3)       # N smallest values from each group    (3 smallest salaries from each city)
gr_city['salary'].value_counts()     # count unique values for each group    (unique salaries in each city)

# Aggregate - custom function
# The custom function should take a sequence of values (Series) and return a single value (the aggregate).
gr_city['salary'].apply(lambda ser : ser )

# ______________________________________________________________________________________________________________________
# Plotting examples
df.plot.scatter(x='age', y='salary')
df.gender.hist()


