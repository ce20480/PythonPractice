'''
plt.plot
'r' or 'k' to change colour of the plot red and black respectively
'o' or '*' style of markers point and stars respectively
'--' or '.' to change style of the line with dashes or dots respectively
linewidth 
markersize
'''
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint

x = randint(-1,11,6)
y = randint(-2,14,6)
x = sorted(np.array(x))
f = sorted(np.array(y))
'''
# normal plotting line graphs
plt.plot(x,y,'-xr', 
         linewidth=3,
        markersize=10,
        label='Data 1')
#legend
plt.legend(loc='best', fontsize=12)
#Axis label
plt.xlabel('$x$',fontsize=20)
plt.ylabel('$y$',fontsize=20)
#Title
plt.title('Simple plot of $f$ against $x$', fontsize=18)
plt.show()
'''
# legends usefulness
# plt.plot(x,f, label='f')
# plt.plot(x,f**2,label='f^2')
# plt.legend(loc='best')
# plt.show()
# subplots section
# plt.subplot(211)# 2 rows 1 column index 1
# plt.plot(x,f,'r')

# plt.subplot(212)# 2 rows 1 column index 2
# plt.plot(x,f,'--b')
# plt.xlim(x[0],x[-1])
# plt.show()
'''
bar plot 
1. create an array with position of x ticks 
2. produce bar plot 
3. replace values x tick value with actual data names
4. axis labels
'''
# year_group = ['B1', 'B2', 'B3', 'M1', 'M2']
# num_students = [500, 332, 425, 300, 200]
# x_pos = np.arange((len(year_group)))
# plt.bar(x_pos, num_students)
# plt.xticks(x_pos, year_group)
# plt.xlabel('year group')
# plt.ylabel('number of students')
# plt.show()
'''
histogram
'''
# 500 values in the range 0 to 100
# R = np.random.randint(0,100,500)
# #Produce histogam with 20 bins,for example 1-5 all the values in between that range will be collected
# n, bins, patches = plt.hist(R,20, facecolor ='green') 
# #add label
# plt.xlabel('value')
# plt.ylabel('frequency')
# plt.show()
'''
scatter
can use plt.plot
or plt.scatter
'''
# plt.plot(x,y, 'ro')
# plt.show()
# plt.scatter(x,y)
# plt.show()

'''
how to save plots
plt.savefig('my-plot.pdf) or .png to save in in the current directory
'''
# plt.plot(x,f)
# plt.savefig('my-plot.pdf')#save fig in current directory
# plt.savefig('my-plot.png')#save fig in current directory
# plt.show()# if called before saving, saved figure will be blank
'''
importing data
csv - comma seperating values 
using numpy
'''
'''
import csv
# data_path = 'signal_data.csv'
data_path = 'Temperature.csv'

with open(data_path, 'r') as f:
    
    #producing plot for singal_data

    reader = csv.reader(f,delimiter=',')
    # data = np.array(list(reader)).astype(float for the signal
    data = list(reader)# not immediately create numpy array since file contains text and numerical values
cities = [d[0] for d in data][1:]# can either do that or [d[0] for d in data[1:]] this removes the blank element from original list rather than created list
data = [d[1:] for d in data] #because d is a singular list d[1:] gets all elements after and including the first element
headers = data[0]
data = np.array(data[1:]).astype(float)#just to check that we dont have mixed type of data

# # 1. array with the position of each bar
x_pos = np.arange(data.shape[1])#gives number of columns of the data

# Width of each bar
W = 0.2

# # 2. Bar plot
for i in range(data.shape[0]):#gives number of rows of the data same as 3 in this case
    plt.bar(x_pos, data[i,:], width=W, label=cities[i])
    x_pos = x_pos + W

# # 3. Replace x ticks with text
# Rotate labels 30 degrees 
plt.xticks(x_pos-W, headers, rotation=30)

# # 4. Add axis labels
plt.xlabel('2007')
plt.ylabel('ave temp deg C')
plt.legend()
plt.show()

#plt.plot(data[0,:], data[1,:]) for signal plotting row 1 against row 2
'''
#numpy method with line graph
data = np.loadtxt( 'Temperature.csv', delimiter=',',
                  skiprows=1, usecols=range(1,7))# have to work with numerical data only

for i in range(data.shape[0]):
    plt.plot(data[i,:])

plt.show()



