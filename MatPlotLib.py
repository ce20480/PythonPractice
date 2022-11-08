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
plt.plot(x,y, 'ro')
plt.show()
plt.scatter(x,y)
plt.show()