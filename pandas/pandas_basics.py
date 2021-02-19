import pandas as pd

# Data frame
# Two dimensional array; a sequence of Series that share same index.
# First column is index from 0 to N (number of records).
# Second and remaining columns are each a Series containing values in that column from 0 to N.
# Each row is also a Series, and can be identified by index number.

# ----------------------------------------------------------------------------------------------------------------------
# Read CSV as dataframe
pd.read_csv('data/olympics.csv')

# Accessing column Series
df.SeriesName                   # Returns Series. Only works if no space in series name
df['SeriesName']                # Returns Series
df[['SeriesOne', 'SeriesTwo']]  # Returns DataFrame. Access multiple series

# Use type() to quickly determine if you're working with Series or DataFrame
type(df.SeriesName)


# Series
# One dimensional array of indexed data.
