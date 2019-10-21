# We have 'simple.html' file in the current working directory. The first step was to open it for reading.
# BeautifulSoup(file_object, parser)
# Takes in file object and parser mode and returns a bs4 object. File object can be obtained by opening any .html file
# with our 'with open() as f:' statement. The parser mode is recommended to be 'lxml' but there are other ones.

from bs4 import BeautifulSoup
import requests
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\4_beautiful_soup")

with open('simple.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#%% print(soup)
#   Printing a bs4 object results in printing all HTML code it contains.
print(soup)                 # Prints all HTML code.
print('\n', type(soup))     # Object is of "bs4.BeautifulSoup" class

#%% soup.prettify()
#   Returns a string of HTML code that bs4 object contains, but formatted with original HTML indentations.
print(soup.prettify())

#%% soup.title
#   Will return a string containing the <title></title> tag and its contents. Will only return one tag which is the
#   first matched tag within the HTML file. The resulting 'match' variable is a bs4 object too.
match = soup.title
print(match)
print('\n', type(match))

#%% soup.title.text
#   Here we are accessing .text attribute of a specific tag. So it will return only the contents of the <title></title>
#   tag without the tag itself around the string. Still returns only the first tag found in HTML file.
match = soup.title.text
print(match)

#%% soup.find('tag', kwargs)
#   soup.find() allows to find a tag with specific attributes in HTML file (as opposed to first matched case).
#   The first argument is the tag we are looking for as a string. e.g. 'div'
#   There are many key-word arguments we can pass to it to specify our search.
#   class_='class' will return HTML tag of a specific class.
#   Most of the time an attribute of a tag matches the keyword (e.g. id='id') but for class_ we use underscore because
#   class is a keyword in Python.
match = soup.find('div', class_='article')
print(match.prettify())

#%% Another example.
article = soup.find('div', class_='article')
print(article.prettify())

#%% We can search the output of the find() function in the same way, because it is still a bs4 object.
article = soup.find('div', class_='article')

headline = article.h2.text
summary = article.p
print(headline)
print(summary)

#%% We could also search the output of a find() function with another find() function because they are both bs4 objects.
body = soup.find('body')
print(body.prettify())

footer = body.find('div', class_='footer')
print(footer.prettify())

paragraph = footer.p.text
print(paragraph)


#%% soup.find_all('tag', kwargs)
#   The method returns a list of bs4 objects which matched the tag search. We can iterate through the result.
articles = soup.find_all('div', class_='article')
print(articles, '\n')
for article in articles: print(article, end='\n\n')

#%% We can loop through soup.find_all('tag', kwargs) directly, since it returns a list of bs4 objects.
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print() # To make space between articles































