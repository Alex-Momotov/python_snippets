# Now that we are familiar with basics of bs4 module, we can substitute our simple.html file with a real file from
# the web. The requests module can pull html code from a website for us.

# requests.get(link)
# Takes a web link as an input and returns a 'response' object.
from bs4 import BeautifulSoup
import requests
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\4_beautiful_soup")

source = requests.get('http://coreyms.com/')
print(source)
print(type(source))

#%% if we pass .text attribute to our response object, it will return a string of the actual HTML code for that page.
source = requests.get('http://coreyms.com/').text
print(source)
print(type(source))

#%% Therefore we can now substitute our simple.html file with this string containing html code to use with bs4 module.
from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

#%% Taking apart a website of articles.
article = soup.find('article')

# Single article
# print(article.prettify())

# Header within single article
# print(article.header.prettify())

# Title within header within single article
print(article.header.h2.text)

# Time within header within single article (time article was published)
print(article.header.p.time.text)

# Author within header within single article
print(article.header.p.find('span', class_="entry-author").text)

# Link to comments within header within single article
print(article.header.p.find('span', class_="entry-comments-link").text)

#%% Extracting summary of a single article
article = soup.find('article')
summary = article.find('div', class_='entry-content').p.text
print(summary)

#%% We can access different attributes of a bs4 tag object in a similar way to a dictionary.
#   Here we parse out link to comments for a single article using .a['href']
article = soup.find('article')
print(article.header.p.find('span', class_="entry-comments-link").a['href'])

#%% This is a complete script to scrape title, summary and time for each article on a single page.

from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.header.h2.text
    print(headline)

    time = article.header.p.time.text
    print(time)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    print()

#%% If some part of our scraper is prone to break, because the page might be missing that element sometimes, then
#   we can put that part of our code in a try-except statement. For example assume an article does not have a time stamp
#   sometimes, then we want to pass None value to that variable.

from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.header.h2.text
    print(headline)

    try:
        time = article.header.p.time.text
    except Exception:
        time = None
    print(time)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    print()

#%% Here we perform the same operation as above, but instead of printing info about each article, we save it to csv

from bs4 import BeautifulSoup
import requests
import csv
import os

os.chdir("C:\\Users\\Sasha\\Coding\\Python\\0. Learning Python\\4_beautiful_soup")

source = requests.get('http://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

with open('articles.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['Headline', 'Time', 'Summary'])

    for article in soup.find_all('article'):

        headline = article.header.h2.text
        time = article.header.p.time.text
        summary = article.find('div', class_='entry-content').p.text

        csv_writer.writerow([headline, time, summary])









