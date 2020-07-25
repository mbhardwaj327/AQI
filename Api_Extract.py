#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pa 
import matplotlib.pyplot as plt


# In[74]:


def avg_data_2013():
    temp_i=0;
    avergae=[]
    
    for rows in pa.read_csv('Data/AQI/aqi2013.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pa.DataFrame(data=rows)
        for index,rows in df.iterrows():
            data.append(rows['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        avergae.append(avg)
        #print(avergae)
    return avergae


# In[ ]:





# In[57]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[68]:


def avg_data_2014():
    temp_i=0;
    avergae=[]
    
    for rows in pa.read_csv('Data/AQI/aqi2014.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pa.DataFrame(data=rows)
        for index,rows in df.iterrows():
            data.append(rows['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        avergae.append(avg)
    return avergae


# In[69]:


def avg_data_2015():
    temp_i=0;
    avergae=[]
    
    for rows in pa.read_csv('Data/AQI/aqi2015.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pa.DataFrame(data=rows)
        for index,rows in df.iterrows():
            data.append(rows['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        avergae.append(avg)
    return avergae


# In[70]:


def avg_data_2016():
    temp_i=0;
    avergae=[]
    
    for rows in pa.read_csv('Data/AQI/aqi2016.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pa.DataFrame(data=rows)
        for index,rows in df.iterrows():
            data.append(rows['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        avergae.append(avg)
    return avergae


# In[71]:


def avg_data_2017():
    temp_i=0;
    avergae=[]
    
    for rows in pa.read_csv('Data/AQI/aqi2017.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pa.DataFrame(data=rows)
        for index,rows in df.iterrows():
            data.append(rows['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        avergae.append(avg)
    return avergae


# In[72]:


def avg_data_2018():
    temp_i=0;
    avergae=[]
    
    for rows in pa.read_csv('Data/AQI/aqi2018.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pa.DataFrame(data=rows)
        for index,rows in df.iterrows():
            data.append(rows['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        avergae.append(avg)
        
    return avergae


# In[75]:


if __name__=="__main__":
    lst2013=avg_data_2013()
    lst2014=avg_data_2014()
    lst2015=avg_data_2015()
    lst2016=avg_data_2016()
    lst2017=avg_data_2017()
    lst2018=avg_data_2018()
    plt.plot(range(0,365),lst2013,label="2013 data")
    plt.plot(range(0,364),lst2014,label="2014 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




