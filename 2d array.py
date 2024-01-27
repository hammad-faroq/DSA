import numpy as np
from array import array
"""This is 1d array having fixed elements and fixed data types"""

arr=array("i",[1,2,3,4,5])
print(arr)
for i in arr:
    print(i)

"""2d array is made by using the numpy module"""
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
def access_element(array,row,column):
    if row>=len(array) or column!=len(array[0]):
        print("index out of range")
    else:
        print(array[row][column])
def transverse_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
# access_element(array,1,9)
# transverse_array(array)
"""All in all,the methods in 1d array and a simple list works the same except that an array has same data structures but lists can have differnet data types """
my_list=[1,2,3,4,5]
print(my_list)
my_list.insert(0,0)
print(my_list)
my_list.append(10)
print(my_list)
my_list.extend([8,9,10])#This will extend the list with other list
print(my_list)
my_list[0:2]=[-1,-2]
print(my_list)
my_list.pop()#This will delete the lsat element
print(my_list)
my_list.pop(1)#this will delete the first element
print(my_list)
del my_list[0]#This will delete the first element
print(my_list)
del my_list[0:3]#Tis slicing also helps to delte and change the values in the list
print(my_list)
my_list.remove(10)
print(my_list)