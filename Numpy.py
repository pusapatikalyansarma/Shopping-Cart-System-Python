#Creating 1D,2D,3D Arrays
import numpy as np
numbers=np.array([1,2,3])
print(numbers)

#2D Arrays
num=np.array([[1,2,3],[4,5,6]])
print(num)

#3D Arrays
r=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(r)

#Zero Matrix
Zeros=np.zeros((3,3))
print(Zeros)

#Matrix of ones
Ones=np.ones((4,4))
print(Ones)

#Identity Matrix
eye=np.eye(4)
print(eye)

#Seed Function
np.random.seed(1)

#Random Integers
q=np.random.randint(1,100,(3,3))
print(q)

#Random Values Between 0and 1
w=np.random.rand(3,3)
#w=np.random.rand(3,3)*99+1 #30th line and this line both are same
print(w)

#Random Choice
e=np.random.choice([10,20,30,40,50,60,70,80,90,100],5)
print(e)
