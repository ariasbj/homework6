#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


import random 

num = 40 
start = 0
end = 100

x = random.sample(range(start, end + 1), num)

num = 40 
start = 0
end = 100

y = random.sample(range(start, end + 1), num)

num = 40
start = 0
end = 100

z = random.sample(range(start, end +1), num)

print(x, y, z)


# In[8]:


fig, axs = plt.subplots(2)
fig.suptitle('Stack Subplots')
axs[0].set_title('Lines')
axs[0].plot(range(40), x, color = 'orange', linewidth = 10)
axs[0].plot(range(40), y, color = 'red', linestyle = 'dashed')

axs[1].set_title('Scatter')
axs[1].scatter(range(40), y, color = 'magenta', marker = 'D')

plt.show()


# In[ ]:




