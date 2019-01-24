# This is a traditional way of importing matlab, because most of what we will be doing is in pyplot
import matplotlib.pyplot as plt
# This uses style from seaborn
from matplotlib import style
style.use('seaborn')
# If we are working in Jupyter Notebook we nee to pass the following statement so it displays correctly:
"%matplotlib inline"    # But without quotes

#%% plt.plot(y)
#   Basic plot function. Can plot list of values against another list of values.
#   If list of values X is ommited then X is automatically set to index array of Y i.e. 0...N-1
#   plt.show() Displays graph to us.
y = [6,4,7,2,6,5,7,4,8,5,9,6,9,8]
plt.plot(y)
plt.show()

#%% plt.plot(x, y)
#   Plots x against y using default line style and colour.
#   plt.grid() Displays grid.
x, y = [1,2,3], [8,2,6]
plt.plot(x,y)
plt.grid()
plt.show()

#%% Plotting multiple sets of data (1st way)
#   We can plot two sets of data using a single plt.plot() statement.
#   Not specifying line colour colours them in different colours.
x, y = [1,2,3], [8,2,6]
x1, y1 = [1,2,3], [2,8,4]
plt.plot(x,y, x1,y1)
plt.show()

#%% Plotting multiple sets of data (2nd way)
#   Use multiple plt.plot() statements.
#   Not specifying line colour colours them in different colours.
x, y = [1,2,3], [8,2,6]
x1, y1 = [1,2,3], [2,8,4]
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()

#%% plt.figure(figsize=(x,y))
#   Creates a new figure.
#   figsize=(x,y) specifies width and height of created figure in inches.
y = [6,4,7,2,6,5,7,4,8,5,9,6,9,8]
plt.figure(figsize=(20, 6))
plt.plot(y)
plt.show()

#%% plt.clf()
#   Clears the current figure. If you are saving many figures we need to either create new figures or clear active one.
#   When we launch it nothing should happen.
y = [6,4,7,2,6,5,7,4,8,5,9,6,9,8]
plt.plot(y)
plt.clf()
plt.show()

#%% plt.savefig('test.png', transparent=boolean)
#   transparent=boolean     Will save the figure with transparent background.
#   Saves figure to a file.
#   Supported formats are: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz
#   plt.savefig() statement should come before plt.show() else saved figure will be blank.
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\6. Matplotlib")
x, y = [1,2,3], [8,2,6]
plt.plot(x,y)
plt.savefig('test.png')
plt.show()

#%% plt.plot(x, y, fmt)
#   fmt is a format string setting colour, marker and line style: '[color][marker][line]' all optional and in any order.
#   Colours:
#   'b' blue    'g' green   'r' red     'c' cyan    'm' magneta     'y' yellow      'k' black       'w' white
#   Markers:
#   '.' dot     ',' pixel      'o' circle      '+' plus       'x' X        '*' star        '2' tri
#   Line Styles:
#   '-' solid       '--' dashed     '-.' dash dot       ':' dotted
y1 = [6,4,7,2,6,5,7,4,8,5,9,6,9,8]
y2 = [1,2,1,2,3,2,1,3,2,1,2,3]
x3, y3 = [1,13], [2,4]

plt.plot(y1, 'bx')
plt.plot(y2, 'g-.')
plt.plot(x3, y3, 'r--')
plt.show()

#%% Some useful keyword arguments:
#   plt.plot(x, y, fmt, linewidth=float)        Regulates line width.           (lw)
#   plt.plot(x, y, fmt, markersize=float)       Regulates marker size.          (ms)
#   plt.plot(x, y, fmt, markeredgewidth=float)  Regulates marker thickness.     (mew)
#   plt.plot(x, y, fmt, alpha=0,5)              Regulates transparency of plotted things, value can be between 0 and 1.
y1 = [6,4,7,2,6,5,7,4,8,5,9,6,9,8]
y2 = [x-1 for x in y1]
x3, y3 = [0,12], [2,3]
x4, y4 = [0,12], [1,4]

plt.plot(y1, 'xr', ms=12, mew=3)
plt.plot(y2, 'xg', ms=4)
plt.plot(x3, y3, 'oc--', lw=2, mew=5)
plt.plot(x4, y4, 'b--', lw=10, alpha=0.6)
plt.show()

#%% By default multiple sets of data are coloured differently using style cycles.
#   Therefore, most of the time no need to specify colour of line or marker.
#   Can change style cycle if really want to.
x = [i for i in range(100)]
y1 = [2*i + 3 for i in x]
y2 = [i + 2 for i in x]
y3 = [4*i - 1 for i in x]
y4 = [5*i - 3 for i in x]
y5 = [6*i - 3 for i in x]

plt.plot(x, y1, x, y2, x, y3, x, y4, x,y5)
plt.show()

#%% plt.title('title')      Gives title to the plot.
#   plt.xlabel('label')     Givex x-label to the plot.
#   plt.ylabel('label')     Givex y-label to the plot.
#   size=fontsize       Keyword argument setting font size. Works for all 3 methods.
#   rotation=degrees    Keyword argument setting text rotation in degrees. Works for all 3 methods.
x, y = [1,2,3], [8,2,6]
plt.plot(x, y)
plt.title('My First Graph', size=18)
plt.xlabel('x-axis', size=16, rotation=45)
plt.ylabel('y-axis', size=16)
plt.show()

#%% plt.plot(x, y, label=str)
#   plt.legend()
#   We can label each plotted line by passing 'label' keyword argument to plot, then creating legend with plt.legend()

x, y = [1,2,3], [8,2,6]
x1, y1 = [1,2,3], [2,8,4]
plt.plot(x, y, label='line1')
plt.plot(x1, y1, label='line2')
plt.legend()
plt.show()

#%% plt.text(x,y,str)
#   Puts text right onto the graph, as an alternative labelling method.
#   Accepts text keywords such as rotation and size.
x, y = [1,10], [2,6]
x1, y1 = [1,10], [4,5]
plt.plot(x, y)
plt.plot(x1, y1)
plt.text(2,4.27, 'line 1', rotation=10, size=16)
plt.text(2.4,3.10, 'line 2', rotation=36, size=16)
plt.show()

#%% Plotting a function
#   First - define a function to be plotted.
#   Second - create a list of spaced values.
#   Your x-values is the spaced values, your x-values is the function on them.
import math
import os
os.chdir("C:\\Users\Sasha\Coding\Python\\0. Learning Python\\6. Matplotlib")

x = [i/10 for i in range(0,140,1)]
y1 = [math.sin(i) for i in x]
y2 = [math.cos(i) for i in x]

plt.plot(y1, 'c--', y2, 'b-')
plt.savefig('sine_cosine.png')
plt.show()

