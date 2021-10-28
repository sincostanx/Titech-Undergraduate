from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(20,15))
ax = fig.add_subplot(111, projection='3d')

data=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range (1,6):
    s="8dir_variable_proba_propagation_for_time"+str(i)+".txt"
    f=open(s,"r")
    while True:
        fx=f.readline()
        if len(fx)==0: break
        l=fx.split()
        countx=0
        for x in l:
            data[countx].append(float(x))
            countx+=1
    f.close()
s=0;e=101
burnt=[]
for i in range(0,5):
    ax.scatter(data[1][s:e],data[0][s:e],data[6][s:e],c='b')
    ax.plot(data[1][s:e],data[0][s:e],data[6][s:e],c='b')
    ax.scatter(data[1][s:e],data[0][s:e],data[8][s:e],c='r')
    ax.plot(data[1][s:e],data[0][s:e],data[8][s:e],c='r')
    check=True
    for j in range(s,e):
        if data[8][j]==0 and check:
            burnt.append(j)
            check=False
    s+=101;e+=101
temp1=[]
temp2=[]
temp3=[]
for x in burnt:
    temp1.append(data[1][x])
    temp2.append(data[0][x])
    temp3.append(data[8][x])
ax.scatter(temp1,temp2,temp3,c='c')
ax.plot(temp1,temp2,temp3,c='c')
"""
for i in range(0,101,5):
    temp=[data[1][i],data[1][i+101],data[1][i+202],data[1][i+303],data[1][i+404]]
    temp2=[data[0][i],data[0][i+101],data[0][i+202],data[0][i+303],data[0][i+404]]
    temp3=[data[6][i],data[6][i+101],data[6][i+202],data[6][i+303],data[6][i+404]]
    ax.plot(temp,temp2,temp3,c='b')
"""
ax.set_xlabel('Probability that neighboring trees catching fire')
ax.set_ylabel('Time needed to completely burn a tree')
ax.set_zlabel('Number of non-burnt tree')
plt.savefig("true_graph.jpg",format='jpg',dpi=300)
#plt.savefig("true_graph.svg",format='svg',dpi=1200)