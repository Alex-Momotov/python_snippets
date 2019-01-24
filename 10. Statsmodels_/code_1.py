import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from scipy.stats.stats import pearsonr

# Returns a tuple of Pearson correlation coefficient and its p-value
pearson_r = pearsonr(x,y)[0]
pearson_p_val = pearsonr(x,y)[1]

# Regression analysis code
x = sm.add_constant(x)
model = sm.OLS(y, x)
results = model.fit()
intercept, gradient = results.params

f_value = results.fvalue
P_f_value = results.f_pvalue
coef_p_val = results.pvalues[1]
r_squared = results.rsquared
adj_r_squared = results.rsquared_adj
t_statistic = results.tvalues[1]
coef_interval = results.conf_int()[1]

# Print the results
print(results.summary())
print('Pearson coeff:'.ljust(22), pearson_r)
print('Pearson coeff p-val:'.ljust(22), pearson_p_val)
print('F-statistic:'.ljust(22), f_value)
print('Prob (F-statistic):'.ljust(22), P_f_value)
print('Coeff P-value:'.ljust(22), coef_p_val)
print('R-squared:'.ljust(22), r_squared)
print('Adj. R-squared:'.ljust(22), adj_r_squared)
print('t-statistic'.ljust(22), t_statistic)
print('Confidence interval'.ljust(22), coef_interval)

#%% Normal distribution
x = np.random.normal(0,1,[5000])
y = np.random.normal(0,1,[5000])
plt.figure(figsize=(8,8))
plt.plot(x,y, 'b.', ms=2)
plt.plot([0,0],[-4,4], 'k--', lw=1)
plt.plot([-4,4],[0,0], 'k--', lw=1)
plt.show()

#%% Horisontal mirror
x = np.random.normal(0,1,[5000])
y = np.random.normal(0,1,[5000])/3
plt.figure(figsize=(8,8))
plt.plot(x, y, 'b.', ms=2)
plt.plot([0,0],[-4,4], 'k--', lw=1)
plt.plot([-4,4],[0,0], 'k--', lw=1)
plt.show()

#%% Vertical mirror
x = np.random.normal(0,1,[5000])/3
y = np.random.normal(0,1,[5000])
plt.figure(figsize=(8,8))
plt.plot(x, y, 'b.', ms=2)
plt.plot([0,0],[-4,4], 'k--', lw=1)
plt.plot([-4,4],[0,0], 'k--', lw=1)
plt.show()

#%% Positive correlation
x = np.random.normal(0,1,[5000])
y = np.random.normal(0,1,[5000])/3+x
plt.figure(figsize=(8,8))
plt.plot(x, y, 'b.', ms=2)
plt.plot([0,0],[-4,4], 'k--', lw=1)
plt.plot([-4,4],[0,0], 'k--', lw=1)
plt.show()

#%% Negative correlation
x = np.random.normal(0,1,[5000])
y = np.random.normal(0,1,[5000])/3 -x
plt.figure(figsize=(8,8))
plt.plot(x, y, 'b.', ms=2)
plt.plot([0,0],[-4,4], 'k--', lw=1)
plt.plot([-4,4],[0,0], 'k--', lw=1)
plt.show()




