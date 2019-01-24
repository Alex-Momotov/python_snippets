#%% Reading from a CSV file
#   CSV stands for "comma separated values"
#   By default delimiter is a comma ','
import os
os.chdir(r"C:\Users\Sasha\Coding\Python\0. Learning Python\3. Working with Files")
import csv
with open('test.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')

    for line in csv_reader:
        print(line)

#%% Make list of lists from a csv file
with open('test.csv', 'r') as f:
    csv_reader = csv.reader(f)
    list_of_lists = list(csv_reader)

print(list_of_lists)

#%% Writing to a csv file
#   To avoid double new line in the end of each line, pass newline='' parameter to open().

things_to_write = [['first_name', 'last_name', 'email'],
                  ['John', 'Doe', 'john-doe@bogusemail.com'],
                  ['Mary', 'Smith-Robinson', 'maryjacobs@bogusemail.com'],
                  ['Dave', 'Smith', 'davesmith@bogusemail.com']]

with open('test_written.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f, delimiter='\t')
    for line in things_to_write:
        csv_writer.writerow(line)

#%% Dictionary-reading from a csv file
#   The file must have field-names in the first line.
#   The fields from the first line become dictionary keys.
#   There are as many dictionaries as there are lines.
import csv
with open('test.csv', 'r') as f:
    csv_reader = csv.DictReader(f, delimiter=',')
    A = list(csv_reader)
    for line in csv_reader:
        print(line)

#%% Dictionary-writing to a csv file
#   We must pass fieldnames parameter to csv.DictWriter which is the list of fieldnames.
#   The format of things_to_write must be a list of dictionaries, where each key corresponds to one key in fieldnames.
#   To avoid double new line in the end of each line, pass newline='' parameter to open().
import csv

field_names = ['first_name','last_name','email']
things_to_write = [{'first_name': 'John', 'last_name': 'Doe', 'email':'john-doe@bogusemail.com'},
                   {'first_name': 'Mary', 'last_name':'Smith-Robinson', 'email':'maryjacobs@bogusemail.com'},
                   {'first_name':'Dave', 'last_name':'Smith', 'email':'davesmith@bogusemail.com'}]

with open('test_written.csv', 'w', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=field_names, delimiter='\t')

    csv_writer.writeheader()
    for line in things_to_write:
        csv_writer.writerow(line)