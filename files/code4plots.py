### Line plot
#%matplotlib inline     # this is automatically done now in ipynb (you don't have to do plt.show())
import matplotlib.pyplot as plt
Years = [1992, 1995, 1997, 2000, 2003, 2005, 2007, 2010, 2012, 2015, 2017]
Prices = [20, 70, 100, 140, 50, 70, 80, 40, 100, 140, 50]
plt.plot(Years, Prices)
plt.xlabel('Year')
plt.ylabel('Real estate Prices (in million US dollars')
#plt.show()
#plt.savefig('image1.jpg')



# Line plot 2
import matplotlib.pyplot as plt

Years = [1992, 1995, 1997, 2000, 2003, 2005, 2007, 2010, 2012, 2015, 2017]
Prices_seoul = [20, 70, 100, 140, 50, 70, 80, 40, 100, 140, 50]
Prices_US = [120, 130, 150, 50, 20, 30, 40, 140, 120, 140, 150]
plt.plot(Years, Prices_seoul)
plt.plot(Years, Prices_US)
plt.xlabel('Year')
plt.ylabel('Real estate Prices (in million US dollars)')
plt.legend(['Seoul', 'US'])
#plt.show()
#plt.savefig('image2.jpg')


# Line plot 2 -- variation
plt.plot(Years, Prices_seoul, linestyle=':', color='r')
plt.plot(Years, Prices_US, linestyle='--', color='b')
plt.xlabel('Year')
plt.ylabel('Real estate Prices (in million US dollars)')
plt.legend(['Seoul', 'US'])


### error plot
import matplotlib.pyplot as plt
Laps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Speed = [30, 28, 27, 25, 20, 15, 12, 12, 11, 9]
Speed_STD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.errorbar(Laps, Speed, yerr=Speed_STD, capsize=5)
plt.xlabel('Number of Laps')
plt.ylabel('Average Speed (km)')
#plt.show()
#plt.savefig('image2-2.jpg')


### fill in plot
import matplotlib.pyplot as plt
import numpy
Laps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Speed = [30, 28, 27, 25, 20, 15, 12, 12, 11, 9]
Speed_STD = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
### Speed_STD_upper = Speed + Speed_STD
### Speed_STD_lower = Speed - Speed_STD
Speed_STD_upper = numpy.array(Speed) + numpy.array(Speed_STD)
Speed_STD_lower = numpy.array(Speed) - numpy.array(Speed_STD)
### you don't have to understand the above!!!!

plt.fill_between(Laps, Speed_STD_upper, Speed_STD_lower, alpha=.2)
plt.plot(Laps, Speed)

plt.xlabel('Number of Laps')
plt.ylabel('Average Speed (km)')
#plt.show()
#plt.savefig('image2-3.jpg')


### Bar plot 1
import matplotlib.pyplot as plt

Name = ['Sam', 'John', 'Rock', 'Joey', 'Ross']
Marks = [85, 30, 90, 35, 60]
plt.bar(Name, Marks, color='green')
plt.xlabel('Name of Students')
plt.ylabel('Makrs in a test')
plt.ylim([0, 100]) # NEW THING!
#plt.show()
#plt.savefig('image3.jpg')


### Scatter plot 1
import matplotlib.pyplot as plt

Weight = [30, 40, 55, 56, 60, 61, 62, 65, 69, 70, 72, 73, 78, 85, 87]
Height = [160, 161, 90, 139, 141, 150, 173, 141, 150, 141, 170, 120, 157, 160, 200]
plt.scatter(Weight, Height, color=blue)
plt.xlabel('Weight')
plt.ylabel('Height')
#plt.show()
#plt.savefig('image4.jpg')


#### Scatter plot 2

import matplotlib.pyplot as plt

Weight = [30, 40, 55, 56, 60, 61, 62, 65, 69, 70, 72, 73, 78, 85, 87]
Height = [160, 161, 90, 139, 141, 150, 173, 141, 150, 141, 170, 120, 157, 160, 200]
Weight2 = [20, 30, 40, 50, 60, 70, 80, 90]
Height2 = [125, 130, 147, 152, 166, 190, 120, 170]
plt.scatter(Weight, Height, color='blue')
plt.scatter(Weight2, Height2, color='red')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.legend(['group1', 'group2'])
#plt.show()
#plt.savefig('image5.jpg')


#### Histogram 
import matplotlib.pyplot as plt
import numpy as np

N_points = 100000
# Generate a normal distribution, center at x=0
x = np.random.randn(N_points)

plt.hist(x)
# plt.hist(x, bins=10)
plt.xlabel('Number')
#plt.show()
#plt.savefig('image6.jpg')



#### Box plot
import matplotlib.pyplot as plt
import numpy as np

N_points = 100000
# Generate a normal distribution, center at x=0
x = np.random.randn(N_points)

plt.boxplot(x)
# plt.hist(x, bins=10)
plt.xlabel('Number')
#plt.show()
#plt.savefig('image7.jpg')



#### Box plot 2
import matplotlib.pyplot as plt
import numpy as np

N_points = 100000
# Generate a normal distribution, center at x=0
x = np.random.exponential(size=N_points)
plt.boxplot(x)
# plt.hist(x, bins=10)
plt.xlabel('Number')
#plt.show()
#plt.savefig('image8.jpg')

### histogram for Boxplot2
import matplotlib.pyplot as plt
import numpy as np

N_points = 100000
# Generate a normal distribution, center at x=0
x = np.random.exponential(size=N_points)
plt.hist(x, bins=100)
#plt.savefig('image8.1.jpg')



##### Violin plot
import matplotlib.pyplot as plt
import numpy as np

N_points = 100000
# Generate a normal distribution, center at x=0
x1 = np.random.randn(N_points)
x2 = np.random.exponential(size=N_points)
#plt.violinplot(x1)
plt.violinplot(x2)
plt.xlabel('Number')
#plt.show()
#plt.savefig('image9.1.jpg')



##### Subplots 1
import matplotlib.pyplot as plt
import numpy as np

N_points = 100000
# Generate a normal distribution, center at x=0
x1 = np.random.randn(N_points)
x2 = np.random.exponential(size=N_points)
plt.subplot(1,2,1)
plt.violinplot(x1)
plt.xlabel('Number')
plt.title('Normal')

plt.subplot(1,2,2)
plt.violinplot(x2)
plt.xlabel('Number')
plt.title('Exponential')
#plt.show()
#plt.savefig('image10.jpg')


##### Subplots 2
import matplotlib.pyplot as plt
import numpy as np

N_points = 100000
# Generate a normal distribution, center at x=0
x1 = np.random.randn(N_points)
x2 = np.random.exponential(size=N_points)
plt.subplot(2,1,1)
plt.violinplot(x1)
plt.xlabel('Number')
plt.title('Normal')

plt.subplot(2,1,2)
plt.violinplot(x2)
plt.xlabel('Number')
plt.title('Exponential')
#plt.show()
#plt.savefig('image10.2.jpg')




##### Subplots 2
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=[2,6])
N_points = 100000
# Generate a normal distribution, center at x=0
x1 = np.random.randn(N_points)
x2 = np.random.exponential(size=N_points)
plt.subplot(2,1,1)
plt.violinplot(x1)
plt.xlabel('Number')
plt.title('Normal')

plt.subplot(2,1,2)
plt.violinplot(x2)
plt.xlabel('Number')
plt.title('Exponential')
#plt.show()
plt.tight_layout()
#plt.savefig('image10.3.jpg')



########### Seaborn
import seaborn as sns
import numpy as np
import pandas as pd

N_points = 100000
# Generate a normal distribution, center at x=0
x1 = np.random.randn(N_points)
x2 = np.random.exponential(size=N_points)

Y = np.concatenate((x1, x2))

mydata = pd.DataFrame({'Y':Y, 
                      'Type':['Normal']*N_points + ['Exponential']*N_points })

sns.violinplot(data=mydata, x='Type', y='Y')
plt.title('Normal and Exponential')

#plt.savefig('image11.jpg')


