import numpy as np
import matplotlib.pyplot as plt

#declare variables and initial conditions  
d,alpha=0.2,10.
xmax,ymax=100,100
dx=dy=1
loop=1000
dt=d*(dx**2.)/alpha
nx=int(xmax/dx);ny=int(ymax/dy)
x=np.linspace(0,nx*dx,nx)
y=np.linspace(0,ny*dy,ny)
T=np.zeros((nx,ny))
T[1:ny-1,1:nx-1]=100.

#Forward in time, Center in space
def fdm(T):
    T[1:ny-1,0]=T[1:ny-1,0]+d*(T[1:ny-1,1]+T[1:ny-1,2]-4*T[1:ny-1,0]+T[0:ny-2,0]+T[2:ny,0]-2*dx*(-10))
    T[1:ny-1,nx-1]=T[1:ny-1,nx-1]+d*(T[1:ny-1,nx-2]+T[1:ny-1,nx-2]-4*T[1:ny-1,nx-1]+T[0:ny-2,nx-1]+T[2:ny,nx-1]-2*dx*(8))
    T[ny-1,1:nx-1]=T[ny-1,1:nx-1]+d*(T[ny-1,2:nx]+T[ny-1,0:nx-2]-4*T[ny-1,1:nx-1]+T[ny-2,1:nx-1]+T[ny-2,1:nx-1]-2*dx*(6))
    T[0,1:nx-1]=T[0,1:nx-1]+d*(T[0,2:nx]+T[0,0:nx-2]-4*T[0,1:nx-1]+T[2,1:nx-1]+T[1,1:nx-1]-2*dx*(-10))
    T[1:ny-1,1:nx-1]=T[1:ny-1,1:nx-1]+d*(T[1:ny-1,2:nx]+T[1:ny-1,0:nx-2]-4*T[1:ny-1,1:nx-1]+T[2:ny,1:nx-1]+T[0:ny-2,1:nx-1])
    return T

#time loop and plotting graph
cnt=0
for n in range(0,loop):
    plt.contourf(x,y,T,cmap='rainbow')
    plt.clim(-100,300)
    plt.colorbar()
    plt.title(n*dt)
    plt.savefig('2_neumann_%05.5d.png'%(cnt))
    plt.clf()
    plt.cla()
    T=fdm(T)
    cnt+=1
