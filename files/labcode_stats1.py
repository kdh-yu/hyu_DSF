
####### 1st CODE (search data file)
from google.colab import files
uploaded = files.upload()


####### 2nd CODE (upload date file)
import io
import pandas as pd
uploadedDATA = pd.read_csv(io.BytesIO(uploaded['skeweddata.csv']))
print(uploadedDATA['a'])


####### 3rd CODE (get statistics)
import scipy.stats
import numpy

print('The mean of this data set is {}.'.format(numpy.mean(uploadedDATA['a'])))
print('The median of this data set is {}.'.format(numpy.median(uploadedDATA['a'])))
print('The standard deviation of this data set is {}.'.format(numpy.std(uploadedDATA['a'])))
print('The IQR of this data set is {}.'.format(scipy.stats.iqr(uploadedDATA['a'])))


# for more stats using python
# Please google libraries, and functions
#  or search https://stackoverflow.com/


####### 4th CODE (binomial in action! -- the python version)

import numpy.random
import matplotlib.pyplot as plt

### (i) Parameters for the random binomial generator
N = 5
theta = .4

### (ii) Generate random binomial data. Just like you picked the stones from the bag!
DATA = []
DATA = [numpy.random.binomial(N, theta) for i in range(50)]

### (iii) Things for plotting, which you don't have to understand for now
plt.hist(DATA, edgecolor='black', align='mid', bins=[-.5,.5,1.5,2.5,3.5,4.5,5.5])
plt.xlim([-.5, 5.5])
plt.show()