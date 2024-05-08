#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 0


# In[20]:


def github() -> str:


    return "https://github.com/rohund/Problem-Set/blob/main/ProblemSet2.py"


# In[21]:


#Exercise 1


# In[22]:


import numpy as np

def simulate_data(seed: int = 481) -> tuple:

    np.random.seed(seed) 
    
   
    X = np.random.normal(loc=0, scale=np.sqrt(2), size=(1000, 3))
    

    e = np.random.normal(loc=0, scale=1, size=(1000, 1))
    
  
    y = 5 + 3*X[:,0] + 2*X[:,1] + 6*X[:,2] + e
    
    return (y, X)


# In[23]:


#Excersise 2


# In[24]:


import numpy as np
import scipy as sp


def estimate_mle(y: np.array, X: np.array) -> np.array:
 
 
    initial_guess = np.ones(4).reshape(-1)
    
  
    result = sp.optimize.minimize(
        fun = linear_regression,
        x0 = initial_guess,
        args = (y, X),
        method='Nelder-Mead'
    )
    
   
    coefficients = result.x
    return coefficients


# In[25]:


def linear_regression(params, y, X):
 
    X = np.c_[np.ones(X.shape[0]).reshape(-1,1), X]
    
    e = y - (X @ params)
    prob_e = (np.exp((-e**2)/2)/(np.sqrt(2 * np.pi)))

    return -np.sum(np.log(prob_e))


# In[26]:


#Exercise 3


# In[27]:


import numpy as np
import scipy as sp



def estimate_ols(y, X):

    
  
    initial_guess = np.ones(4).reshape(-1)
    
   
    result = sp.optimize.minimize(
        fun = ols_residuals,
        x0 = initial_guess,
        args = (y, X),
        method='Nelder-Mead'
    )
    
   
    coefficients = result.x
    
    return coefficients



# In[28]:


def ols_residuals(beta, y, X):


    X = np.c_[np.ones(X.shape[0]).reshape(-1,1), X]
    
    e = y - (X @ beta)
    e_sums = np.sum(np.square(e))
    return np.sum(np.square(e))

