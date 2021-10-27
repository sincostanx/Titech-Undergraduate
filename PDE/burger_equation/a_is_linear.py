import numpy as np
import matplotlib.pyplot as plt

#declare variables and initial conditions    
v,a=0.1,0.1
dt=0.1
xmax,ymax=25,25
dx=dy=1
loop=750
nx=int(xmax/dx)
ny=int(ymax/dy)
x=np.linspace(0,nx*dx,nx)
y=np.linspace(0,ny*dy,ny)
T=np.zeros((nx,ny))
T[15,15]=1

#Forward in time, Backward in Space, Center for 2nd Differentiation
def fdm(T):
    T=T+dt*(v*(np.roll(T,-1,axis=0)+np.roll(T,1,axis=0)+np.roll(T,-1,axis=1)+np.roll(T,1,axis=1)-4*T)/(dx**2.)-a*(2*T-np.roll(T,1,axis=0)+np.roll(T,1,axis=1)/dx))
    return T

#time loop and plotting graph
cnt=0
for n in range(0,loop):
    plt.contourf(x,y,T,cmap='rainbow',vmin=np.amin(T),vmax=np.amax(T))
    plt.colorbar()
    plt.title(n*dt)
    plt.savefig('burger_1_%05.5d.png'%(cnt))
    plt.clf()
    plt.cla()
    T=fdm(T)
    cnt+=1
