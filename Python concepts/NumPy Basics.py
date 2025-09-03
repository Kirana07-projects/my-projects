#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[5]:


# Creation of a random array of values
ar = np.random.rand(3,2)
ar


# In[6]:


# Creation of four matrices of random numbers

ar = np.random.rand(4, 3, 2)
ar


# In[7]:


# Creation of an array of input values given by me
ar1 = np.array([[2,3], [3,4]])
ar1


# In[11]:


# Check the data type of an array that I created
type(ar)
type(ar1)


# In[12]:


# Check the data type of the elements of an array
ar.dtype
ar1.dtype


# In[16]:


# Check the shape of an array 
ar1.shape


# In[17]:


# Check the size of an array 
ar1.size


# In[21]:


# Slicing
ar[0]


# In[22]:


ar1[0]


# In[ ]:


# Reverse operation and give the last row of the array
ar1[-1]


# MATHEMATICAL OPERATIONS

# In[24]:


# Creation of another array
ar2 = np.array([[4,5], [6,3]])
ar2


# In[25]:


# Addition
np.add(ar1, ar2)


# In[27]:


# Subtraction
np.subtract(ar2,ar1)


# In[28]:


# Multiplication
np.multiply(ar1, ar2)


# In[29]:


# Division
np.divide(ar1,ar2)


# In[30]:


# dot product - multiplication of each element in the matrix and summing them up 
np.dot(ar1,ar2)


# In[33]:


# Vectorization - for eg; i want to add 5 to each element of my matrix 
ar3 = ar2 + 5
ar3


# In[34]:


# Square root of a number
np.sqrt(2)


# In[35]:


# Square root of an array
np.sqrt(ar3)


# In[36]:


# Power of a number
np.power (12, 4)


# In[37]:


# Power of an array 
np.power (ar3, 2)


# SORTING OPERATIONS

# In[40]:


#Sorting in ascending order
np.sort(ar3)


# In[41]:


np.sort(ar3)[::-1] #[start:stop:step]


# In[42]:


# Delete a row or column of a matrix 
np.delete(ar3, 1, axis = 0)   #Second element represents the which row or column, axis represents where a row (0) or column (1) must be deleted


# KEY CONCEPTS FROM THE COURSE 

# In[44]:


# Arange - generates evenly spaced values within the given range
a = np.arange(0, 10, 2) # always it is start, end (does not print the end value), step size
print("Arange", a)


# In[48]:


# linspace - Creates an array of evenly spaced values between two numbers, including the end points
b = np.linspace(0, 10, 5) #(start, end, no:of values)
print("Linspace", b)


# In[50]:


c = np.linspace(0, 10, 2) #(start, end, no:of values)
print("Linspace", c)


# In[51]:


# Slicing and broadcasting
# Slicing - allows access to a subset of an array using index ranges
d = np.array([[10, 20, 30], [40, 50, 60]])
d


# In[52]:


print("Slicing", d[1:4])


# In[55]:


print("Slicing", d[:2, :2]) #two rows and two columns


# In[57]:


# Broadcasting
d[1:4] = 100
print("After Broadcasting", d)


# In[58]:


# Mean, SD and percentile 
print("Mean", np.mean(d))
print("Std. Dev", np.std(d))
print("90th percentile", np.percentile(d,90))

