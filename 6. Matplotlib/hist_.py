import matplotlib.pyplot as plt
import random
#%% plt.hist(x)
#   x is either a single array or a sequence of arrays which are not required to be of the same length.
#   It is a single arrtibute frequency data which makes each histogram.
#   Histogram displays ocurrance of each value (frequency) in a specific range.
data = [1,1,2,2,2,3,4,4,5,5,5,5,5,6,6,7,7,7,8,9,9,9,9]
plt.hist(data)
plt.show()

#%% Useful keyword artuments.
#   color='k'       Single colour format string, or a sequence of colours if many datasets.
#   bins=num        Bins is the number of 'bars' per each histogram.
#   alpha=num       Transparency of each histogram. Values are between 0 and 1.
#   range=(min,max) The lower and upper range of the bins. Lower and upper outliers are ignored.
#   density=True    If True, the first element of the return tuple will be the counts normalized to form a probability
#   density, i.e., the area (or integral) under the histogram will sum to 1. This is achieved by dividing the count by
#   the number of observations times the bin width and not dividing by the total number of observations. If stacked is
#   also True, the sum of the histograms is normalized to 1.
data = [random.gauss(100,15) for i in range(100000)]
plt.hist(data, bins=200, alpha=0.65, density=True, color='k')
plt.show()

#%% weights=seq
#   An array of weights, of the same shape as x. Each value in x only contributes its associated weight towards the bin
#   count (instead of 1). If normed or density is True, the weights are normalized, so that the integral of the density
#   over the range remains 1.
data = [random.gauss(100,15) for i in range(10000)]
data.sort()
weight_arr = [0.2 for i in range(5000)]+[1 for i in range(5000)]
plt.hist(data, bins=80, alpha=0.65, density=True, weights=weight_arr)
plt.show()

#%% cumulative=boolean
#   Each bin now displays cumulative frequency.
data = [random.gauss(0,100) for i in range(10000)]
plt.hist(data, bins=200, cumulative=True)
plt.show()

#%% histtype=keyword
#   This is the main kwarg for specifying how we want to plot multiple data sets (more than one histogram).
#   ‘stepfilled’ generates a lineplot that is by default filled. We will want to use this most of the time.
#   'bar' is a traditional bar-type histogram. If multiple data are given the bars are arranged side by side.
#   ‘barstacked’ is a bar-type histogram where multiple data are stacked on top of each other.
#   ‘step’ generates a lineplot that is by default unfilled.
data = [random.gauss(100,15) for i in range(10000)]
data2 = [random.gauss(100,40) for i in range(10000)]
data = [data, data2]
plt.hist(data, 100, alpha=0.65, density=True, histtype='stepfilled')
plt.show()

#%% When plotting multiple datasets it is easier to pass kwards in sequences
#   data = sequence of sequences
#   color = sequence
#   label = sequence
data = [random.gauss(100,15) for i in range(10000)]
data2 = [random.gauss(100,40) for i in range(10000)]
data = [data, data2]
colors = ['r','k']
labels = ['one','two']
plt.hist(data, 100, alpha=0.65, density=True, histtype='stepfilled', color=colors, label=labels)
plt.legend()
plt.show()

