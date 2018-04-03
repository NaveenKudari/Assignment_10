
# coding: utf-8

# In[12]:


#for window of 3 moving average with using numpy inbuilt function convolve
import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
 
def movingaverage (values, window):
    weights = np.repeat(1.0, window)/window
    ma = np.convolve(values, weights, 'valid')
    return ma

y=[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
 
yMA = movingaverage(y,3)
print(yMA)


# In[11]:


#for window of 3 moving average without using numpy inbuilt function
xa=[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
def movingaverage(array,window):
    for n in range (len(array)-window+1):
        print(np.mean(array[n:n+window]))
        
movingaverage(xa,3)
    

