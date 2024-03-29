# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:16:47 2020

@author: rundo
"""
import scipy.constants as spc
import numpy as np
from matplotlib import pyplot as plt
from Q1d_function import Euler_Cromer as ec
from Q1d_function import Euler_Cromer_GR as gr


#Take initial values, and convert into SI unit
x_0 = 0.47 * spc.au
y_0 = 0
vx_0 = 0
vy_0 = 8.17 * spc.au / 31622400
dt = 31622400 * 0.0001
t = 31622400

#Simulation
result  = ec(x_0, y_0, vx_0, vy_0, dt, t)           #Newton
result_gr  = gr(x_0, y_0, vx_0, vy_0, dt, t)        #GR


#Convert back into AU & year
x = [i / spc.au for i in result[0]]
y = [i / spc.au for i in result[1]]
vx = [i * 31622400 / spc.au for i in result[2]]
vy = [i * 31622400 / spc.au for i in result[3]]

x_gr = [i / spc.au for i in result_gr[0]]
y_gr = [i / spc.au for i in result_gr[1]]




#Plot the orbit
plt.plot(x,y,label='Newton')
plt.plot(x_gr,y_gr,label='GR')
plt.legend()
plt.scatter(0,0,color='red')
plt.text(0.02,0,'Sun')
plt.xlabel('$x$ (AU)')
plt.ylabel('$y$ (AU)')
plt.title('Orbit, $x$ vs $y$')


