import pandas as pd
import numpy as np
import random as rand
pd.set_option('display.max_columns', 200)
pd.set_option('display.min_rows', 60)
pd.set_option('display.width', 4000)

def create_df_with_missing_vals():
    columns = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    df = pd.DataFrame([[rand.randint(0, 9) for i in range(10)] for j in range(30)], columns=columns)
    for i in range(50):
        row = rand.randint(0, df.shape[0] - 1)
        col = rand.randint(0, df.shape[1] - 1)
        df.iloc[row, col] = rand.choice([np.nan, None, 'NA', 'missing'])
    return df

# Create sample dataframe
df = create_df_with_missing_vals()

# Missing values in pandas
# Pandas considers missing values as either None or np.nan (NaN).

# ______________________________________________________________________________________________________________________
# Count missing values
df.isna().sum()         # In each df column
df['one'].isna().sum()  # In specific column

# Count non-missing values
df.info()   # Count non-null (neither np.nan nor None) values per column
            # Also show data type - 'object' usually means string

# Boolean mask where values are missing
df.isna()           # on df
df['one'].isna()    # on series

# ______________________________________________________________________________________________________________________
# Remove missing values
df.dropna()     # Will remove all rows that have at least one value missing - None or np.nan (NaN).
                # subset=['col', col1]  Only remove rows if missing values are in specified columns.
                # inplace=True          Make changes inplace.

# ______________________________________________________________________________________________________________________
# Replace missing values
df.fillna('GOOD_VAL', inplace=True)         # Replace missing values (np.nan or None) in entire df, with a given value.

# Replace custom missing values - with pandas recognised missing values
df.replace('missing', None, inplace=True)   # For example replace 'missing' string with None

# Replace custom missing values - with value of your choice
df.replace('NA', -1, inplace=True)

# ______________________________________________________________________________________________________________________
# Cast column to another type
df['one'] = '5'                     # Create first column as string
df['one'] = df['one'].astype(float)             # Cast to float - using ser.astype(type)
df['one'] = df['one'].apply(lambda x : int(x))  # Cast to int - using ser.apply(func)











