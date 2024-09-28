# Consider the below code to answer further questions:
import numpy as np
list_ = ['1','2','3','4','5']
array_list = np.array(object = list_)

# Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code
# to print the data types of both the variables.
# yes there is a difference.
# print(array_list.dtype)
# print(type(list_))

# Q2. Write a code to print the data type of each and every element of both the variables list_ and
# arra_list.
# for j in list_:
#     print(type(j))
# print (array_list.dtype)

# Q3. Considering the following changes in the variable, array_list:
# array_list = np.array(object = list_, dtype = int)
# Will there be any difference in the data type of the elements present in both the variables, list_ and
# arra_list? If so then print the data types of each and every element present in both the variables, list_
# and arra_list.
# print(array_list.dtype)
# for j in list_:
#     print(type(j))

# Consider the below code to answer further questions:
# import numpy as np
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
# num_array = np.array(object = num_list)
# Q4. Write a code to find the following characteristics of variable, num_array:
# (i) shape
arr1=np.array(num_list)
# print(arr1.shape)
# (ii) size
# print(arr1.size)

# Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array
# creation function.
# print(np.zeros((3,3)))
# arr2=[[1,2,3],[4,5,6],[7,8,9]]
# for j in range(3):
#     for k in range(3):
#         arr2[j][k]=0
# print(np.array(arr2))

# [Hint: The size of the array will be 9 and the shape will be (3,3).]

# Q6. Create an identity matrix of shape (5,5) using numpy functions?
# [Hint: An identity matrix is a matrix containing 1 diagonally and other elements will be 0.]
# print(np.eye(5))

# a=np.random.randint(1,5,(5,5))
# for j in range(5):
#     a[j][j]=1
#     a[j][j+1:5]=0
#     a[j][0:j]=0
# print(a)
    
