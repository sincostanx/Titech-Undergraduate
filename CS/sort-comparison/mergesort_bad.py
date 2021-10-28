#
# MERGE SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# recursively,
#   cut the array into two halves: left, right
#   sort each half
#   merge both halves
#

#
# Non-destructive sort:
#
# array is unchanged
# returns a sorted copy
#
def merge(a,b):
    res=[];i=j=0
    while i<len(a) or j<len(b):
        if i==len(a): res+=[b[j]];j+=1
        elif j==len(b): res+=[a[i]];i+=1
        elif a[i]<b[j]: res+=[a[i]];i+=1
        else: res+=[b[j]];j+=1
    return res
def sort(d):
    t=d
    def mergesort(l,r):
        if l==r: return [t[l]]
        m=(l+r)>>1
        return merge(mergesort(l,m),mergesort(m+1,r))
    return mergesort(0,len(d)-1)