#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


def estimate_pi(N):
   
    points = np.random.rand(N, 2)
    distances = np.linalg.norm(points, axis=1)
    inside_circle = distances[distances <= 1]
    pi_estimate = 4 * len(inside_circle) / N
    
    return pi_estimate


N_values = [int(1e3), int(1e4), int(1e5), int(1e6)]


for N in N_values:
    pi_estimate = estimate_pi(N)
    print(f"N = {N}: Estimated π = {pi_estimate}")


N = int(1e4)
pi_estimate = estimate_pi(N)
points = np.random.rand(N, 2)
distances = np.linalg.norm(points, axis=1)
inside_circle_indices = np.where(distances <= 1)[0]

plt.figure(figsize=(6, 6))
plt.scatter(points[:, 0], points[:, 1], c='blue', s=5, label='Outside Circle')
plt.scatter(points[inside_circle_indices, 0], points[inside_circle_indices, 1], c='red', s=5, label='Inside Circle')
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Estimating π using Monte Carlo Method')
plt.xlabel('X')
plt.ylabel('Y')
plt.text(0.05, 0.9, f'Estimated π = {pi_estimate:.5f}', transform=plt.gca().transAxes)
plt.legend()
plt.show()


# In[ ]:




