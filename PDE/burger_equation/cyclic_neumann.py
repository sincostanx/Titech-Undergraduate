import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

#declare variables and initial conditions    
v,a=0.1,0.1
dt=0.1
xmax,ymax=25,25
dx=dy=1
loop=1000
nx=int(xmax/dx)
ny=int(ymax/dy)
x=np.linspace(0,nx*dx,nx)
y=np.linspace(0,ny*dy,ny)
T=np.zeros((nx,ny))
T[20,20]=1

#Forward in time, Backward in Space, Center for 2nd Differentiation
def fdm(T):
    T[0,:]=T[0,:]+dt*(v*(T[2,:]+T[1,:]+np.roll(T[0,:],-1,axis=0)+np.roll(T[0,:],1,axis=0)-4*T[0,:])/(dx**2.)-a*(2*T[0,:]-T[2,:]+np.roll(T[0,:],1,axis=0)/dx))
    T[ny-1,:]=T[ny-1,:]+dt*(v*(T[ny-2,:]+T[ny-2,:]+np.roll(T[ny-1,:],-1,axis=0)+np.roll(T[ny-1,:],1,axis=0)-4*T[ny-1,:])/(dx**2.)-a*(2*T[ny-1,:]-T[ny-2,:]+np.roll(T[ny-1,:],1,axis=0)/dx))
    T[1:ny-1,:]=T[1:ny-1,:]+dt*(v*(T[0:ny-2,:]+T[2:ny,:]+np.roll(T[1:ny-1,:],-1,axis=1)+np.roll(T[1:ny-1,:],1,axis=1)-4*T[1:ny-1,:])/(dx**2.)-a*(2*T[1:ny-1,:]-T[0:ny-2,:]+np.roll(T[1:ny-1,:],1,axis=1)/dx))
    return T

#time loop and plotting graph
cnt=0

X,Y=np.meshgrid(x,y)

for n in range(0,loop):
    """
    #2d plotting
    plt.contourf(x,y,T,cmap='rainbow',vmin=np.amin(T),vmax=np.amax(T))
    plt.colorbar()
    plt.title(n*dt)
    plt.savefig('xburger_3_%05.5d.png'%(cnt))
    plt.clf()
    plt.cla()
    """
    
    #3d plotting
    fig=plt.figure()
    ax=fig.gca(projection='3d')
    surface=ax.plot_surface(X,Y,T.reshape(X.shape),cmap='rainbow',vmin=np.amin(T),vmax=np.amax(T))
    ax.set_title(n*dt)
    ax.view_init(elev=10., azim=45.)
    fig.colorbar(surface, shrink=1, aspect=5)
    plt.savefig('x3d_burger_3_%05.5d.png'%(cnt))
    plt.cla()
    plt.clf()
    
    
    T=fdm(T)
    cnt+=1
