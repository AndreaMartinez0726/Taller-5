import numpy as np 
import matplotlib.pylab as plt
from scipy.linalg import expm 

######### Punto 2 #######

H= np.array([[0.0,0.0,0.0,0.0],[0.0, -2.0, 1.0, 0.0 ],[0.0,1.0, -2.0, 0.0 ],[0.0,0.0,0.0,4.0]])
print H

####### Punto 3#######
T=1.0
N=10000
t= T/N
U= expm(-1j*t*H)
##### Punto 4#######

x= (np.array([0.0,1.0,1.0,0.0]))*1/(2.0)**(1.0/2.0)
print x
####### Punto 5 ####

Un= np.linalg.matrix_power(U,N)
x0= np.linalg.solve(Un,x)
print x0

##### Punto 6 #######
comp= np.matmul(Un,x0)
