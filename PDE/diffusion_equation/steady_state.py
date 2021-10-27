import numpy as np
import matplotlib.pyplot as plt

#declare variables and initial conditions
alpha,g=1,9.81
xmax,ymax=100,100
dx=dy=2
nx=int(xmax/dx)
ny=int(ymax/dy)
x=np.linspace(0,nx*dx,nx)
y=np.linspace(0,ny*dy,ny)
T=np.zeros((nx,ny))
T[:,0]=1.;T[0,:]=1.;T[:,-1]=1.;T[-1,:]=1.

#construct and solve system of equations
A=np.zeros((nx*ny,nx*ny))
B=np.zeros(nx*ny)
for i in range(0,ny):
    for j in range(0,nx):
        if(i==0 or j==0 or i==ny-1 or j==nx-1): 
            A[i*ny+j,i*ny+j]=1;B[i*ny+j]=T[i,j]
            continue
        A[i*ny+j,i*ny+j]=-4
        A[i*ny+j,i*ny+j+1]=1
        A[i*ny+j,i*ny+j-1]=1
        A[i*ny+j,i*ny+j-ny]=1
        A[i*ny+j,i*ny+j+ny]=1
        B[i*ny+j]=g/alpha
ans=np.linalg.solve(A,B)

#plot 3D graph
X,Y=np.meshgrid(x,y)
fig=plt.figure()
ax=fig.gca(projection='3d')
surface=ax.plot_surface(X,Y,ans.reshape(X.shape),cmap='Blues',vmin=np.amin(ans),vmax=np.amax(ans))
ax.set_title('steady state')
ax.view_init(elev=10., azim=10.)
fig.colorbar(surface, shrink=1, aspect=5)
plt.savefig('1_1_final.png')