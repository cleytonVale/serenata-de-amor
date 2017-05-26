
# coding: utf-8

# # Suspicious reimbursements analysis
# 
# We are finding suspicious reimbursements since last year, but we did not know how many reimbursements we already find that are suspicious, and how we had impacted the Chamber of Deputies.
# 
# This study is trying to find the numbers of all those months exploring the Chamber of Deputies CEAP reimbursements.
# Here, we will be using two datasets:
# * `2017-05-25-suspicious.xz` a recent dataset generated by rosie that contains **all reimbursements**, and rosie's classifiers, asigned with true if they have some suspicion. 
# * `2017-05-25-supicious-true-subset.csv` that, based on the first dataset, gets a **subset of only the reimbursements that already contain true** in one classifier.
# 
# Let's see what we get :)

# In[1]:

import pandas as pd
import numpy as np

suspicions = pd.read_csv('../data/2017-05-25-suspicions.xz', low_memory=False)
suspicions.head()


# In[2]:

len(suspicions)


# So, as we can se there are **1.619.213 reimbursements** that we are already judging.
# 
# There is the other subset that we want to analyse.

# In[3]:

suspicions_subset = pd.read_csv('../data/2017-05-25-suspicions-true-subset.csv', low_memory=False)
suspicions_subset.head()


# This dataset contains only the `document_id` and the classifiers result of the reimbursements that have some suspicion.

# In[4]:

len(suspicions_subset)


# With that we can conclude that in a dataset with **1.619.213 reimbursements**, **8216 of them** have some suspicion.
# 
# We can say that Rosie already find suspicions in (8216/1619213) = 0.005% of the reimbursements.

# ## Percentual of any classifier
# 
# We can calculate what is the percentual of appearance of classifiers, what appears more than other and so on. Remembering that one reimbursement can have more than one suspicion.

# ### Meal Price Outlier
# Here we will calculate how many suspicious reimbursements we find with the `meal_price_outlier` classifier.

# In[5]:

len(suspicions_subset.query('meal_price_outlier == True'))


# From all the 8216 suspicious reimbursements, 2158 of them have suspicious meal prices.

# ### Over Monthly Subquota Limit
# Here we will calculate how many suspicious reimbursements we find with the `over_monthly_subquota_limit` classifier.

# In[6]:

len(suspicions_subset.query('over_monthly_subquota_limit == True'))


# From all the 8216 suspicious reimbursements, 18 of them have suspicion on passing the monthly subquota.

# ### Suspicious Traveled Speed Day
# Here we will calculate how many suspicious reimbursements we find with the `suspicious_traveled_speed_day` classifier.

# In[7]:

len(suspicions_subset.query('suspicious_traveled_speed_day == True'))


# From all the 8216 suspicious reimbursements, 792 of them have suspicion on passing the monthly subquota.

# ### Invalid CPNJ/CPF
# Here we will calculate how many suspicious reimbursements we find with the `invalid_cnpj_cpf` classifier.

# In[8]:

len(suspicions_subset.query('invalid_cnpj_cpf == True'))


# From all the 8216 suspicious reimbursements, 16 of them have suspicion on passing the monthly subquota.

# ### Election Expenses
# Here we will calculate how many suspicious reimbursements we find with the `election_expenses` classifier.

# In[9]:

len(suspicions_subset.query('election_expenses == True'))


# From all the 8216 suspicious reimbursements, 13 of them have suspicion on passing the monthly subquota.

# ### Irregular Companies Classifier
# Here we will calculate how many suspicious reimbursements we find with the `irregular_companies_classifier` classifier.

# In[10]:

len(suspicions_subset.query('irregular_companies_classifier == True'))


# From all the 8216 suspicious reimbursements, 5240 of them have suspicion on passing the monthly subquota.

# Remembering that all of them are suspicions, and we need to check if the suspicion is real or no :)