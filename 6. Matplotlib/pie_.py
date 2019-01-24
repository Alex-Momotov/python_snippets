import matplotlib.pyplot as plt
import matplotlib as mpl
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\6. Matplotlib")

#%% plt.pie(slice_values)
#   Creates a simple pie chart defined by values in the given array slice_values.
#   labels=categorie    This labels each slice with a text.
#   plt.axis('equal')   Makes sure the pie chart is round, as opposed to elipse.
#   autopct='%0.1f%%'   Writes percentage values inside slices, you can specify decimal places in format string.
#   shadow=boolean      Gives the pie chart a shadow.
#   colors=array        Takes in an array of colours then iterates through them for the pie chart.
companies = ['Facebook','Google','Amazon','Microsoft','Apple','AMD','Intel','Twitter']
revenue = [300,700,400,500,560,200,340,120]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
plt.axis('equal')
plt.pie(revenue, labels=companies, autopct='%0.1f%%', shadow=True, colors=colors)
plt.show()

#%% explode=array
#   The array consists of values 0 to 1 for each pie slice. It defines how far each slice will be drawn out.
#   radius=num      Defines radius of pie chart, can use it together with plt.figure(figsize=(,)) to make sure the pie
#   chart fits into the figure.


companies = ['Facebook','Google','Amazon','Microsoft','Apple','AMD','Intel','Twitter']
revenue = [300,700,400,500,560,200,340,120]
plt.figure(figsize=(10,10))
plt.axis('equal')
plt.pie(revenue, labels=companies, autopct='%0.1f%%', explode=[0.1,0.12,0.13,0.14,0,0,0,0], radius=0.8)
plt.savefig('p_chart.png', transparent=True)
plt.show()

