#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Excercise 0


# In[2]:


def github() -> str:

    return "https://github.com/rohund/Problem-Set/blob/main/ProblemSet5.py"


# In[3]:


#Exercise 1


# In[5]:


import requests
from bs4 import BeautifulSoup

def scrape_code(url: str = "https://lukashager.netlify.app/econ-481/01_intro_to_python") -> str:
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    code_blocks = [x.text for x in soup.find_all('code', class_ = 'sourceCode python')]
    
    code_string = ''
    
    for block in code_blocks:
        code = block.strip()
        
        if not code.startswith('%'):
            code_string += code + '\n'
    
    return code_string.strip()

lecture_code = scrape_code()
print(lecture_code)


# In[ ]:




