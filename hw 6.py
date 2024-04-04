#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import matplotlib.pyplot as plt


# In[8]:


a = 16.02
b = 0.1124
R = 0.083144

pressure = np.linspace(1, 10, 100)
volume = np.linspace(10, 30, 100)
pressure_grid, volume_grid = np.meshgrid(pressure, volume)

temp_grid = (pressure_grid + a / volume_grid**2) * (volume_grid - b) / (R * 1)

plt.figure(figsize = (10, 6))
plt.pcolormesh(pressure_grid, volume_grid, temp_grid, cmap = 'plasma', shading = 'auto', vmin = 200, vmax = 400)
plt.colorbar(label = 'Temp_grid')
plt.xlabel('Pressure (bar)')
plt.ylabel('Volume (L)')
plt.title('Temperature for One Mole of Acetone (P + a n^2/V^2)(V - nb) = nRT')

plt.show()


# In[6]:


pip install numpy


# In[ ]:




