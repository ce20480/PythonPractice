import numpy as np
'''
numpy saves time 
'''
# pure python 
x1 = [x for x in range(2,7)]
y1 = [a+2 for a in x1]
x =  np.array(x1)# 1-D array
y = x + 2
print(y1, y)

nums2 = np.array([[2,4,6], [8,10,12], [14,16,18], [14,16,18]])#2-D array
C = nums2[1:3,1:]#take rows 1,2 and all columns exlcuding column 0
# print(nums2, nums2[0,1], C)#nums[rows,columns]

nums3 = np.array([[[2,4,6], [8,10,12], [14,16,18]],
                 [[3,4,8], [2,2,2], [9,8,1]]])
# print(nums3[0,1], nums3[0,1,2]) #nums[matrix,rows,columns]

x3 = np.arange(1,10)# array from 1-9
z = np.zeros(5)# gives n amount of zeros
z2 = np.zeros((5,2))# give n amount of zeroes as a tuple
y3 = np.ones((2,2))# gives n amount of ones as a tuple
u = np.linspace(1,10,10)# gives n amount of equally spaced values
i = np.eye(4)# nxn I matrix
# or to create the array you can first create 1-D array then re-shape into 2-D
x = np.arrange(0,20)#start inlcusive, end exlcusive
x = x.reshape(4,5)

