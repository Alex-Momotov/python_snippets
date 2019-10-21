import matplotlib.pyplot as plt
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\matplotlib")

#%% plt.bar(categories, height)
#   Plots bar chart. Categories can be strings or numbers.
#   Height determines height of each category bar.
companies = ['Facebook','Google','Amazon','Microsoft','Apple','AMD','Intel','Twitter']
revenue = [300,700,400,500,560,200,340,120]
plt.bar(companies, revenue)
plt.show()

#%% plt.bar(categories, height, width)
#   Width is an optional argument. It specifies width of each bar. It can either be scalar - to represent width of each
#   bar or can be a list representing width of each invididual bar.
companies = ['Facebook','Google','Amazon','Microsoft','Apple','AMD','Intel','Twitter']
revenue = [300,700,400,500,560,200,340,120]
widths = [0.3,0.2,0.4,0.5,0.2,0.6,0.4,0.5]
plt.figure(figsize=(8,3))
plt.bar(companies, revenue, widths)
plt.show()

#%% Useful keyword arguments.
#   color='b' blue    'g' green   'r' red     'c' cyan    'm' magneta     'y' yellow      'k' black       'w' white
#   edgecolor='b', 'g', 'r', 'c', 'm', 'y', 'k', 'w' or '#997EFF'
#   linewidth=number    Line width of bars.     (lw)
companies = ['Facebook','Google','Amazon','Microsoft','Apple','AMD','Intel','Twitter']
revenue = [300,700,400,500,560,200,340,120]
plt.figure(figsize=(8,3))
plt.bar(companies, revenue, color='#997EFF', edgecolor='k', lw=2)
plt.show()

#%% Stacked bar chart.
#   To make a stacked bar chart we need to first of all add another attribute value for each category (second_att).
#   Then we need to call plt.bar() function two times. The second call should specify 'bottom' kwarg as the values
#   of the first attribute. This makes sure second set of bars moves higher and bars don't overlap.
companies = ['Facebook','Google','Amazon','Microsoft','Apple','AMD','Intel','Twitter']
revenue = [300,700,400,500,560,200,340,120]
second_att = [10,200,200,300,260,100,140,20]
plt.bar(companies, revenue)
plt.bar(companies, second_att, bottom=revenue)
plt.show()

#%% Bars attributes next to each other.
#   It is more convenient to import numpy for this because we can add values to numpy array quickly.
#   We need to create numpy array indexing positions of categories.
#   plt.xticks(positions, categories) labels positions of bars with given category array. Takes rotation and size args.
#   Pass positions (instead of categories) to each of the plt.bar(pos, height, width) functions.
#   Alter position slightly to space out the bars. Also change width of bars to make them fit.
#   Can also add labels to each data set with label='text' then pass plt.legend() statement.
import numpy as np
companies = ['Facebook','Google','Amazon','Microsoft','Apple','AMD','Intel','Twitter']
first_att = [300,700,400,500,560,200,340,120]
second_att = [10,200,200,300,260,100,140,20]
positions = np.arange(len(companies))
width = 0.4

plt.xticks(positions, companies, rotation=25, size=10)
plt.bar(positions+0.2, first_att, width, label='Title')
plt.bar(positions-0.2, second_att, width, label='Body')
plt.legend()
plt.show()



