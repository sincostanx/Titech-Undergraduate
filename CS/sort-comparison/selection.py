
#
# SELECTION SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# conceptually, consider two arrays: sorted, unsorted
# initially,
#   sorted   = []
#   unsorted = array
# iteratively,
#   remove the smallest element of unsorted
#   add it at the end of sorted
#
# NB: in the code below, index i represents the "border"
# between sorted and unsorted.
#

def sort(d):
    t=d
    return sort_inline(t)
def sort_inline(d):
    n=len(d)
    for i in range (0,n):
        idx=i
        for j in range (i+1,n):
            if d[j]<d[idx]: idx=j
        d[i],d[idx]=d[idx],d[i]
    return d