# Basic analytics

# Series.value_counts()
# Returns count of unique values in the Series. By default ignores None values, so pass dropna=False to avoid that.
df.Athlete.value_counts(dropna=False)