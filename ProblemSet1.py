#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 0 


# In[ ]:


def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/<rohund>/<Problem-Set-1>/blob/main/<filename.py>"


# In[ ]:


#Exercise 2


# In[3]:


def evens_and_odds(n: int) -> dict:
    """
    Returns a dictionary with the sum of even and odd numbers less than n.
    
    Args:
    n (int): A natural number.
    
    Returns:
    dict: A dictionary with keys 'evens' and 'odds' representing the sum of even and odd numbers less than n respectively.
    """
    evens_sum = sum(i for i in range(n) if i % 2 == 0)
    odds_sum = sum(i for i in range(n) if i % 2 != 0)
    return {'evens': evens_sum, 'odds': odds_sum}

# Test
print(evens_and_odds(4))  # Output: {'evens': 2, 'odds': 4}


# In[4]:


#Exercise 3


# In[7]:


from typing import Union
from datetime import datetime

def time_diff(date_1: str, date_2: str, out: str = 'float') -> Union[str, float]:
    """
    Calculates the time difference between two dates.
    
    Args:
    date_1 (str): The first date in the format 'YYYY-MM-DD'.
    date_2 (str): The second date in the format 'YYYY-MM-DD'.
    out (str): Specifies the output format. Can be 'float' or 'string'. Default is 'float'.
    
    Returns:
    Union[str, float]: Depending on the 'out' parameter, returns either a float representing the time difference in days,
    or a string indicating the time difference.
    """
    # Convert date strings to datetime objects
    date_1 = datetime.strptime(date_1, '%Y-%m-%d')
    date_2 = datetime.strptime(date_2, '%Y-%m-%d')
    
    # Calculate the absolute time difference in days
    time_difference = abs((date_1 - date_2).days)
    
    # Output based on the 'out' parameter
    if out == 'string':
        return f"There are {time_difference} days between the two dates"
    else:
        return time_difference

# Test
print(time_diff('2020-01-01', '2020-01-02', 'float'))  # Output: 1
print(time_diff('2020-01-03', '2020-01-01', 'string'))  # Output: "There are 2 days between the two dates"


# In[ ]:


#Exercise 4


# In[8]:


def reverse(in_list: list) -> list:
    """
    Returns the list in reverse order.
    
    Args:
    in_list (list): Input list.
    
    Returns:
    list: The input list in reverse order.
    """
    reversed_list = []
    # Traverse the input list in reverse order and append elements to the reversed list
    for i in range(len(in_list) - 1, -1, -1):
        reversed_list.append(in_list[i])
    return reversed_list

# Test
print(reverse(['a', 'b', 'c']))  # Output: ['c', 'b', 'a']


# In[ ]:


#Exercise 5


# In[9]:


def prob_k_heads(n: int, k: int) -> float:
    """
    Calculate the probability of getting exactly k heads in n coin flips.

    Args:
    n (int): Number of coin flips.
    k (int): Number of heads.

    Returns:
    float: Probability of getting exactly k heads.
    """
    # Probability of getting a single head
    p_head = 0.5
    
    # Calculate the binomial coefficient (n choose k)
    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)
    
    # Calculate the probability using the binomial probability formula
    probability = binomial_coefficient(n, k) * (p_head ** k) * ((1 - p_head) ** (n - k))
    
    return probability

# Test the function
print(prob_k_heads(1, 1))  # Output: 0.5

