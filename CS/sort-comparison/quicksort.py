import random
#
# QUICKSORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# recursively,
#   take one value from the array as pivot
#   split the remainder of the array into two arrays:
#      left array with values smaller than pivot
#      right array with values larger than pivot
#   sort left and right independently
#   combine left, pivot, right into a sorted array
#
# NB: in practice, the way to chose the pivot is very
# significant to ensure good performance. However, in
# this lecture, we make a naive choice in order to keep
# the discussion simple and focus instead on the core
# idea of the algorithm.

#
# Non-destructive sort:
#
# array is unchanged
# returns a sorted copy
#
def sort(d):
    def partition(l,r):
        idx=(random.randint(0,r-l))+l
        d[l],d[idx]=d[idx],d[l]
        p=d[l];i=l+1;j=r
        while i<=j:
            while i<=j and d[i]<=p: i+=1
            while j>=i and d[j]>=p: j-=1
            if i<=j: d[i],d[j]=d[j],d[i]
        d[l],d[j]=d[j],d[l]
        return j
    def qsort(l,r):
        if l>=r: return
        p=partition(l,r)
        qsort(l,p-1);qsort(p+1,r)
    qsort(0,len(d)-1)
    return d
