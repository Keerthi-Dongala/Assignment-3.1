#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
a=pd.read_csv("df3.csv")
a


# In[4]:


a.info()


# In[5]:


a.head()


# In[10]:


a.plot.scatter(x='a',y='b',c='red',edgecolor="black",s=40,figsize=(10,3))


# In[12]:


a['a'].plot.hist(edgecolor="black")


# In[19]:


a['a'].plot.hist(alpha=0.43,bins=25,color="red",edgecolor="white")


# In[39]:


import matplotlib.pyplot as plt
a[['a','b']].plot.box(color="red")
plt.grid()


# In[38]:


import matplotlib.pyplot as plt
a['d'].plot.kde(color="red")
plt.grid()


# In[37]:


import matplotlib.pyplot as plt
a['d'].plot.kde(linewidth=4,linestyle='--',color="red")
plt.grid()


# In[43]:


import matplotlib.pyplot as plt
a.loc[0:30].plot.area(alpha=0.3)
plt.grid()


# In[44]:


import matplotlib.pyplot as plt
a.loc[0:30].plot.area(alpha=0.4)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.grid()


# In[ ]:




