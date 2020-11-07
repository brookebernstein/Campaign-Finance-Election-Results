#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import pandas, numPy, & dataset
import pandas as pd
import numpy as np
path = "C:\candidatesummaryaction1.csv"


# In[2]:


# Briefly review the data
seg = pd.read_csv(path)
seg.head(10)


# In[3]:


# Retrieve info on data set
seg.info()


# In[4]:


# Describe the numerical columns of the data set
seg.describe()


# In[5]:


# Retrieve a list of column names for dropping
seg.columns


# In[6]:


# Drop unncessary columns
seg = seg.drop(columns = ['can_nam', 'can_off_dis', 'can_str1', 'can_str2', 'can_cit', 'can_zip', 'ind_ite_con', 'ind_uni_con', 'oth_com_con', 'tra_fro_oth_aut_com','can_loa', 'oth_loa', 'tot_loa', 'off_to_ope_exp', 'off_to_fun', 'off_to_leg_acc', 'oth_rec', 'tot_rec', 'exe_leg_acc_dis', 'fun_dis', 'tra_to_oth_aut_com', 'can_loa_rep', 'oth_loa_rep', 'tot_loa_rep', 'ind_ref', 'par_com_ref','oth_com_ref','tot_con_ref', 'tot_dis', 'deb_owe_by_com', 'deb_owe_to_com'])
seg.columns


# In[7]:


# Review updated data set to ensure unncessary columns are dropped
seg.head(5)


# In[8]:


# Retrieve info on updated data set
seg.info()


# In[9]:


# Describe the updated numerical columns of the data set
seg.describe()


# In[10]:


# Change blank values in the winner column to No (N)
seg['winner'] = seg['winner'].fillna('N')


# In[11]:


# Determine which columns have NA values
seg.isna()


# In[12]:


# Drop non-numerical rows that have NA values
seg = seg.dropna(subset = ['can_inc_cha_ope_sea'])
seg.isna()


# In[13]:


# Fill in other applicable missing values with 0
# Not sure if missing values are due to those values equaling 0 or because they are unkown, assuming the former
seg = seg.fillna(0)
seg.isna()


# In[14]:


# Retrieve info on updated data set
seg.info()


# In[15]:


# Convert numerical values to float
# ind_con
seg['ind_con'] = seg.ind_con.str.replace(',', '')
seg['ind_con'] = seg.ind_con.str.replace('$', '')
seg['ind_con']= seg.ind_con.astype(float)
# par_com_con
seg['par_com_con'] = seg.par_com_con.str.replace(',', '')
seg['par_com_con'] = seg.par_com_con.str.replace('$', '')
seg['par_com_con'] = seg.par_com_con.astype(float)
# tot_con
seg['tot_con'] = seg.tot_con.str.replace(',', '')
seg['tot_con'] = seg.tot_con.str.replace('$', '')
seg['tot_con'] = seg.tot_con.astype(float)
# ope_exp
seg['ope_exp'] = seg.ope_exp.str.replace(',', '')
seg['ope_exp'] = seg.ope_exp.str.replace('$', '')
seg['ope_exp'] = seg.ope_exp.str.replace('(', '-')
seg['ope_exp'] = seg.ope_exp.str.replace(')', ' ')
seg['ope_exp'] = seg.ope_exp.astype(float)
# can_con
seg['can_con'] = seg.can_con.str.replace(',', '')
seg['can_con'] = seg.can_con.str.replace('$', '')
seg['can_con'] = seg.can_con.astype(float)
# oth_dis
seg['oth_dis'] = seg.oth_dis.str.replace(',', '')
seg['oth_dis'] = seg.oth_dis.str.replace('$', '')
seg['oth_dis'] = seg.oth_dis.str.replace('(', '-')
seg['oth_dis'] = seg.oth_dis.str.replace(')', '')
seg['oth_dis'] = seg.oth_dis.astype(float)
# cas_on_han_beg_of_per
seg['cas_on_han_beg_of_per'] = seg.cas_on_han_beg_of_per.str.replace(',', '')
seg['cas_on_han_beg_of_per'] = seg.cas_on_han_beg_of_per.str.replace('$', '')
seg['cas_on_han_beg_of_per'] = seg.cas_on_han_beg_of_per.str.replace('(', '-')
seg['cas_on_han_beg_of_per'] = seg.cas_on_han_beg_of_per.str.replace(')', '')
seg['cas_on_han_beg_of_per'] = seg.cas_on_han_beg_of_per.astype(float)
# cas_on_han_clo_of_per
seg['cas_on_han_clo_of_per'] = seg.cas_on_han_clo_of_per.str.replace(',', '')
seg['cas_on_han_clo_of_per'] = seg.cas_on_han_clo_of_per.str.replace('$', '')
seg['cas_on_han_clo_of_per'] = seg.cas_on_han_clo_of_per.str.replace('(', '-')
seg['cas_on_han_clo_of_per'] = seg.cas_on_han_clo_of_per.str.replace(')', '')
seg['cas_on_han_clo_of_per'] = seg.cas_on_han_clo_of_per.astype(float)
# net_con
seg['net_con'] = seg.net_con.str.replace(',', '')
seg['net_con'] = seg.net_con.str.replace('$', '')
seg['net_con'] = seg.net_con.str.replace('(', '-')
seg['net_con'] = seg.net_con.str.replace(')', '')
seg['net_con'] = seg.net_con.astype(float)
# net_ope_exp
seg['net_ope_exp'] = seg.net_ope_exp.str.replace(',', '')
seg['net_ope_exp'] = seg.net_ope_exp.str.replace('$', '')
seg['net_ope_exp'] = seg.net_ope_exp.str.replace('(', '-')
seg['net_ope_exp'] = seg.net_ope_exp.str.replace(')', '')
seg['net_ope_exp'] = seg.net_ope_exp.astype(float)


# In[16]:


# Fill newly exposed NA values with 0
seg = seg.fillna(0)


# In[17]:


# Describe the properties of the table usuing numPy or pandas
# Type of seg
type(seg)


# In[18]:


# Number of rows & columns 
seg.shape


# In[19]:


# Info on data set
seg.info()


# In[20]:


# Description of numerical columns
seg.describe()


# In[21]:


# Description of non-numerical columns
seg.describe(include=np.object)

