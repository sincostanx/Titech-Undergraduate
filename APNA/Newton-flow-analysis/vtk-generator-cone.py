import math
import numpy as np
d=[];countx=0
lmax=20;kmax=20;jmax=1
icnx=1.;icny=1.;icnz=1.
cnr=0.3
cnl=1.0
dcnphi=2.0*math.pi/float(kmax-1)
dcnl=cnl/float(lmax-1)
x=np.zeros((jmax+1,kmax+1,lmax+1), dtype=float)
y=np.zeros((jmax+1,kmax+1,lmax+1), dtype=float)
z=np.zeros((jmax+1,kmax+1,lmax+1), dtype=float)
f = open("cone_case1.vtk", "w")
f.write("# vtk DataFile Version 4.0\ntest\nASCII\n\n")
f.write("DATASET STRUCTURED_GRID\nDIMENSIONS {0} {1} {2}\n".format(lmax,kmax,jmax))
f.write("POINTS {0} float\n".format(lmax*kmax*jmax))

j=1
for l in range (1,lmax+1):
    for k in range(1,kmax+1):
        dcnr=(cnl-dcnl*float(l-1))*(cnr/cnl)
        x[j][k][l]=icnx+dcnr*math.cos(dcnphi*float(k-1))
        y[j][k][l]=icny+dcnr*math.sin(dcnphi*float(k-1))
        z[j][k][l]=icnz+dcnl*float(l-1)
        f.write("{0} {1} {2}\n".format(x[j][k][l],y[j][k][l],z[j][k][l]))
        
f.write("\nCELL_DATA {0}\n".format(jmax*(kmax-1)*(lmax-1)))
f.write("SCALARS Cp float\n")
f.write("LOOKUP_TABLE default\n")
flx=1.0;fly=0.0;flz=0.0
cp=np.zeros((jmax+1,kmax+1,lmax+1), dtype=float)
nvx=np.zeros((jmax+1,kmax+1,lmax+1), dtype=float)
nvy=np.zeros((jmax+1,kmax+1,lmax+1), dtype=float)
nvz=np.zeros((jmax+1,kmax+1,lmax+1), dtype=float)
for l in range(1,lmax):
    for k in range(1,kmax):
        v1x=x[j][k+1][l+1]-x[j][k][l]
        v1y=y[j][k+1][l+1]-y[j][k][l]
        v1z=z[j][k+1][l+1]-z[j][k][l]
        
        v2x=x[j][k][l+1]-x[j][k+1][l]
        v2y=y[j][k][l+1]-y[j][k+1][l]
        v2z=z[j][k][l+1]-z[j][k+1][l]
        
        nvx[j][k][l]=v1y*v2z-v1z*v2y
        nvy[j][k][l]=v1z*v2x-v1x*v2z
        nvz[j][k][l]=v1x*v2y-v1y*v2x
        
        anv=math.sqrt(nvx[j][k][l]**2+nvy[j][k][l]**2+nvz[j][k][l]**2)
        nvx[j][k][l]/=anv
        nvy[j][k][l]/=anv
        nvz[j][k][l]/=anv
        
        afl=math.sqrt(flx**2+fly**2+flz**2)
        
        cp[j][k][l]=2.0*((flx*nvx[j][k][l]+fly*nvy[j][k][l]+flz*nvz[j][k][l])/afl)**2
        if (flx*nvx[j][k][l]+fly*nvy[j][k][l]+flz*nvz[j][k][l]>=0): cp[j][k][l]=0.0
        
        f.write("{0}\n".format(cp[j][k][l]))
f.close()