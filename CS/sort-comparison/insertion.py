
#
# INSERTION SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# conceptually, consider two arrays: sorted, unsorted
# initially,
#   sorted   = []
#   unsorted = array
# take element elt from unsorted one by one
#   insert elt into sorted and move it down
#   until it reaches its correct position
#
# NB: in the code below, index i represents the "border"
# between sorted and unsorted.


def sort(d):
    t=d
    return sort_inline(t)
    #return sort_optimized(t)
def sort_inline(t):
    for i in range(len(t)):
        for j in range(i-1,-1,-1):
             if t[j]>t[j+1]: t[j],t[j+1]=t[j+1],t[j]
    return t
def sort_optimized(t):
    for i in range(len(t)):
        j=i-1
        while j>=0 and t[j]>t[j+1]: t[j],t[j+1]=t[j+1],t[j];j-=1
    return t
