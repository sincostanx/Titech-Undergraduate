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
def sort(d):
    def merge(l,m,r):
        i=l;j=m+1;k=0;temp=d[l:r+1]
        while i<=m or j<=r:
            if i>m: temp[k]=d[j];j+=1
            elif j>r: temp[k]=d[i];i+=1
            elif d[i]<d[j]: temp[k]=d[i];i+=1
            else: temp[k]=d[j];j+=1
            k+=1
        for z in range(0,len(temp)): d[l+z]=temp[z]
    def mergesort(l,r):
        if l==r: return
        m=(l+r)>>1
        mergesort(l,m);mergesort(m+1,r);merge(l,m,r)
    mergesort(0,len(d)-1)
    return d