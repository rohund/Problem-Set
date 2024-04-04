#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 0 


# In[1]:


def github() -> str:
    """
    Connecting to GitHub repository
    """

    return "https://github.com/rohund/Problem-Set/blob/main/ProblemSet1%20(1).py"


# In[4]:


#Exercise 2


# In[2]:


def evens_and_odds(n: int) -> dict:
    """
    Returns a dictionary with the sum of even and odd numbers less than n.
    
    """
    evens_sum = sum(i for i in range(n) if i % 2 == 0)
    odds_sum = sum(i for i in range(n) if i % 2 != 0)
    return {'evens': evens_sum, 'odds': odds_sum}


print(evens_and_odds(4)) 


# In[4]:


#Exercise 3


# In[3]:


from typing import Union
from datetime import datetime

def time_diff(date_1: str, date_2: str, out: str = 'float') -> Union[str, float]:
    """
    Calculates the time difference between two dates.

    """
    date_1 = datetime.strptime(date_1, '%Y-%m-%d')
    date_2 = datetime.strptime(date_2, '%Y-%m-%d')
    
    time_difference = abs((date_1 - date_2).days)
    
    if out == 'string':
        return "There are " + str(time_difference) + " days between the two dates"
    else:
        return time_difference

print(time_diff('2020-01-01', '2020-01-02', 'float'))  
print(time_diff('2020-01-03', '2020-01-01', 'string'))  


# In[6]:


#Exercise 4


# In[7]:


def reverse(in_list: list) -> list:
    """
    Returns the list in reverse order.
 
    """
    reversed_list = []
  
    for i in range(len(in_list) - 1, -1, -1):
        reversed_list.append(in_list[i])
    return reversed_list
    
print(reverse(['a', 'b', 'c']))  


# In[11]:


#Exercise 5


# In[5]:


def prob_k_heads(n: int, k: int) -> float:
    """
    Calculate the probability of getting exactly k heads in n coin flips.

    """
    p_head = 0.5
    
    n_minus_k_fac = 1
    for i in range(1,n-k+1):
        n_minus_k_fac *= i

    n_choose_k = 1
    for i in range(k+1, n+1):
        n_choose_k *= i
    n_choose_k /= n_minus_k_fac
    
    probability = n_choose_k * (p_head ** k) * ((1 - p_head) ** (n - k))
    
    return probability

print(prob_k_heads(4, 1))  

