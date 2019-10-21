import pandas as pd
import numpy as np
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\2_basics_advanced")

#%% pd.DataFrame(dict)
#   Makes a pandas dataframe from a dictionary. Naming a dataframe as 'df' is a convention.
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,64,34],
             'Bounce_Rate':[65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)

#%% Printing out a dataframe
#   print(df)               Will print out entire dataframe.
#   print(df.head(n=5))     Will print out only first n number of lines, default is 5.
#   print(df.tail(n=5))     Will print only n last lines from the bottom, default is 5.
print(df)
print(df.head(2))
print(df.tail(2))

#%% df.set_index('Day')         (This step is optional)
#   Returns a new dataframe which is indexed by a given column in our dataframe.
#   Need to remember to set our dataframe equal to the the returned dataframe.
#   Also remember not to do this operation more than once.
df = df.set_index('Day')
print(df)

#%% df['Visitors']
#   df.Visitors
#   Both ways can be used to reference a single column in dataframe.
print(df['Visitors'])
print(df.Visitors)

#%% df[['col_1', 'col_2']]
#   This is a way to reference multiple columns at once.
#   Need to write column names in a list and pass it into df[]
print(df[['Bounce_Rate', 'Visitors']])

#%% df.column.tolist()
#   Converts a specific dataframe column to a list.
D = df.Day.tolist()
V = df.Visitors.tolist()
print(D)
print(V)

#%% np.array(df)
#   Converts a Pandas dataframe to numpy.
arr = np.array(df)
print(arr)

#%% np.array(df.column)
#   Converts a specified single column of a dataframe to Numpy array.
arr = np.array(df.Bounce_Rate)
print(arr)
print(type(arr))

#%% np.array(df[['col_1', 'col_2']])
arr = np.array(df[['Visitors','Bounce_Rate']])
print(arr)

#%% pd.read_csv('file.csv')
#   Returns a dataframe object made from a CSV file
#   index_col=n     Specifies that index column will be nth column
df = pd.read_csv('AAPL.csv', index_col=0)
print(df.head())

#%% df.to_csv(newFile.csv)
#   Saves dataframe to a CSV file
df.to_csv('newFile.csv')

#%% df.to_csv('newfile.csv', header=True)
#   Setting header=False kwarg will save raw data without column titles in first row
df.to_csv('newFile_no_header.csv', header=False)

#%% pd.read_csv('AAPL.csv', names=['str1', 'str2', 'str1'], index_col=0)
#   names=[list of names] will assign new column names when reading CSV file without column names
df = pd.read_csv('newFile_no_header.csv', names=['Day', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Vol'], index_col=0)
print(df.head())

#%% df.columns
#   Returns columns in a dataframe
df = pd.read_csv('AAPL.csv', index_col=0)
print(df.columns)

#%% df.columns = [new column names as list]
#   To rename columns use attribute df.columns and assign a list of new names to it.
df.columns = ['Day', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Vol']
print(df.head())

#%% df.to_html('file.html')
#   Saves df as an html file. The way HTML format displays data is quite neat.
df = pd.read_csv('AAPL.csv')
df.to_html('example.html')

#%% pd.read_html(link)
#   Will return a list of potential tables from a link itself. We can then index the list to extract needed table as df
df = pd.read_html('http://bexley-is-bonkers.co.uk'
                  '/local_taxes/league_table/2017.php')[0]
print(df[[0,1,2,3]])



