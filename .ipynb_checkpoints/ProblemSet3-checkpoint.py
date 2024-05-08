#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise 0


# In[ ]:


def github() -> str:

    return ""https://github.com/rohund/Problem-Set/blob/main/ProblemSet3.py"


# In[4]:


#Exercise 1


# In[59]:


def import_yearly_data(years: list) -> pd.DataFrame:
    
    dfs = pd.DataFrame()
   
    for year in years:
        temp = pd.read_excel(f"https://lukashager.netlify.app/econ-481/data/ghgp_data_{year}.xlsx", sheet_name = 'Direct Emitters', index_col = False, skiprows = 3)
        temp["year"] = year
        dfs = pd.concat([dfs, temp], ignore_index = True)

    return dfs


# In[18]:


#Exercise 2


# In[86]:


import pandas as pd

def import_parent_companies(years: list) -> pd.DataFrame:

    dfs = pd.DataFrame()

    for year in years: 
        temp = pd.read_excel(f"https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb", sheet_name = year, index_col = False)
        temp['year'] = year
        dfs = pd.concat([dfs, temp], ignore_index = True)

    dfs = dfs.dropna(how = 'all')
    return dfs


# In[ ]:


#Excercise 3


# In[51]:


import pandas as pd

def n_null(df: pd.DataFrame, col: str) -> int:

    return df[col].isnull().sum()


# In[39]:


#Exercise 4


# In[82]:


import pandas as pd

def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:

    merged_data = pd.merge(emissions_data, parent_data, 
                           left_on=['year', 'Facility Id'], 
                           right_on=['year', 'GHGRP FACILITY ID'], 
                           how='left')

    cleaned_data = merged_data[['Facility Id', 'year', 'State', 'Industry Type (sectors)',
                                'Total reported direct emissions', 'PARENT CO. STATE', 
                                'PARENT CO. PERCENT OWNERSHIP']]

    cleaned_data.columns = map(str.lower, cleaned_data.columns)

    return cleaned_data


# In[ ]:


#Excercise 5


# In[96]:


import pandas as pd

def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:

    aggregated = df.groupby(group_vars).agg({
        'total reported direct emissions': ['min', 'median', 'mean', 'max'],
        'parent co. percent ownership': ['min', 'median', 'mean', 'max']
    }, as_index = True)
    
 
    aggregated = aggregated.sort_values(by=('total reported direct emissions', 'mean'), ascending=False)
    
    return aggregated

