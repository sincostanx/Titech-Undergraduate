import numpy as np
import matplotlib.pyplot as plt

#declare variables and choose Courant number
c=.10
dx,u=1.,1.
dt=c*dx/u
loop=int(600/dt+2)
xmax=100
x=np.arange(0.,xmax+dx,dx)

#initialize function / g is another function used in CIP method only.
f0=np.zeros(x.shape[0])
f0[(x>=40.)&(x<=60.)]=1.
f=np.zeros((4,x.shape[0]))
f[:]=f0
g=(f[3]-np.roll(f[3],1,axis=0))/dx

#calculate iup and dxiup / xi is a variable used in CIP method only.
iup=-int(np.sign(u))
dxiup=iup*dx
xi=-1.*u*dt

#analytical solution
def analytic(f0,t):
    f=np.roll(f0,int(u*t),axis=0)
    return f

#upwind scheme
def upwind(f):
    f=f+u*dt*(np.roll(f,-1*iup,axis=0)-f)/dx
    return f

#Leith method / 2nd order Lagrange Interpolation
def leith(f):
    a=(np.roll(f,-1,axis=0)+np.roll(f,1,axis=0)-2*f)/(2*dx**2.)
    b=(np.roll(f,-1,axis=0)-np.roll(f,1,axis=0))/(2*dx)
    c=f
    f=a*(u*dt)**2-b*u*dt+c
    return f

#CIP
def CIP(f,g):
    a=-2*(np.roll(f,-1*iup,axis=0)-f)/(dxiup)**3.+(g+np.roll(g,-1*iup,axis=0))/(dxiup**2.)
    b=-3*(f-np.roll(f,-1*iup,axis=0))/(dxiup)**2.-(2.*g+np.roll(g,-1*iup,axis=0))/dxiup
    f=a*xi**3.+b*xi**2.+g*xi+f
    g=3*a*xi**2.+2*b*xi+g
    return f,g

#information used when plotting graphs
cl=['black','red','green','blue']
method=['analytic','upwind','leith','CIP']
time=[10,200,400,600,loop*dt]
cnt=0

#time loop and plotting graph
for n in range(0,loop):
    if n*dt>=time[cnt]:
        plt.clf()
        plt.cla()
        fig=plt.figure()
        ax=fig.add_subplot(111)
        for i in range(0,4):
            ax.plot(x,f[i],color=cl[i],label=method[i])
        plt.ylim([0.,1.2])
        plt.xlim([0.,100.])
        plt.legend()
        plt.title('Time: %04.3f'%(n*dt))
        plt.savefig('advection_%04d.png'%(time[cnt]))
        cnt+=1
    f[0]=analytic(f0,n*dt)
    f[1]=upwind(f[1])
    f[2]=leith(f[2])
    f[3],g=CIP(f[3],g)
    