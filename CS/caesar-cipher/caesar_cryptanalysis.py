"""
The program uses an array (hashx) to count the number of each lower case alphabets.
Based on the given information in the slide, the most frequent letter is 'e'.
Therefore, the key used to encrypt the message can be calculated from the distance
from position of letter 'e'. Note that the modulo operator is used to handle negative value of key.
"""
import sys
def enc(k,x):
    l=list(x.encode("ascii"))
    for i in range(len(l)): 
        if 97<=l[i]<=122: l[i]=(l[i]-97+k)%26+97
    return bytes(l).decode("ascii")
def dec(k,x):
    return enc(-k,x)
l=[x.rstrip() for x in sys.stdin]
hashx=[0]*26
for y in l:
    for x in y:
        if 'a'<=x<='z': hashx[ord(x)-97]+=1
k=(hashx.index(max(hashx))-4+26)%26
for y in l: print(dec(k,y))