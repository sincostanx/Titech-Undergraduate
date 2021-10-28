def sort(array):
    #itoa
    d=[];n=len(array);maxx=0
    for x in array:
        k=x;t=[]
        while k: t+=[k%10];k//=10
        d+=[t];maxx=max(len(t),maxx)
    for x in d:
        while len(x)<maxx: x+=[0]
    #sort
    hashx=[[]]*10
    num=[i for i in range (0,n)]
    for i in range(0,maxx):
        for j in range (0,10): hashx[j]=[]
        for j in range (0,n): hashx[d[num[j]][i]]+=[num[j]]
        countx=0
        for j in range (0,10):
            for x in hashx[j]:
                num[countx]=x;countx+=1
    #atoi
    return [array[x] for x in num]
    