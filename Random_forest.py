#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pa
import numpy as np
import matplotlib.pyplot as plt
import seaborn as se
import csv

# In[3]:


dataset=pa.read_csv('C:/Users/91912/Downloads/AIR1/real_combine2.csv')


# In[4]:


dataset


# In[5]:


dataset=dataset.drop(columns='SLP',axis=1)


# In[6]:


dataset


# In[15]:


for i in dataset.columns:
    dataset.drop(dataset.loc[dataset[i]=="-"].index,axis=0,inplace=True)


# In[16]:


dataset.isnull().sum()


# In[11]:


dataset=dataset.dropna()



# In[17]:


dataset


# In[18]:


dataset['VM']=dataset['VM'].astype('float')
#dataset.to_csv(r'C:\Users\91912\Downloads\AIR1\real_combine2.csv',index=False)


# In[19]:
#for rows in dataset:
    #print(rows)

dataset.corr()


# In[20]:


dataset.dtypes


# In[21]:


from sklearn.model_selection import train_test_split


# In[22]:


X=dataset.iloc[:,:-1]


# In[23]:


X


# In[24]:


Y=dataset.iloc[:,-1]


# In[26]:


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33,random_state=0)


# In[28]:


se.pairplot(dataset)


# In[29]:


corrmat=dataset.corr()
feature_importance=corrmat.index
plt.figure(figsize=(20,20))
p=se.heatmap(dataset[feature_importance].corr(),annot=True,cmap="RdYlGn")


# In[31]:


from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor


# In[35]:


ran=RandomForestRegressor()


# In[32]:


n_estimators=[int(x) for x in np.linspace(start=100,stop=1200,num=12)]
max_depth=[int (x) for x in np.linspace(start=5,stop=30,num=6)]
max_features=['auto','sqrt']
min_samples_leaf=[1,2,5,10]
min_samples_split=[2, 5, 10, 15, 100]


# In[34]:


parameter={'n_estimators':n_estimators,
           'max_depth':max_depth,
           'max_features':max_features,
           'min_samples_leaf':min_samples_leaf,
           'min_samples_split':min_samples_split}


# In[36]:


random_for=RandomizedSearchCV(ran,param_distributions=parameter,cv=5,n_iter=100,verbose=2,random_state=42,n_jobs=1,scoring='neg_mean_squared_error')


# In[38]:


random_for.fit(X_train,Y_train)


# In[39]:


random_for.best_estimator_


# In[41]:


random_for.best_score_


# In[42]:


Y_pre=random_for.predict(X_test)


# In[43]:


se.distplot(Y_test-Y_pre)


# In[45]:


import pickle


# In[46]:


# open a file, where you ant to store the data
file = open('random_forest_regression_model.pkl', 'wb')

# dump information to that file
pickle.dump(random_for, file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




