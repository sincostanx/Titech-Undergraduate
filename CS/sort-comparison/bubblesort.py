
#
# BUBBLE SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# conceptually, consider two arrays: sorted, unsorted
# initially,
#   unsorted = array
#   sorted   = []
# repeatedly
#   scan through the unsorted array, moving larger elements up
#   until no swap occurs during a scan
#
# NB: in the code below, index n represents the "border"
# between unsorted and sorted.
def sort(d):
    t=d
    return sort_inline(t)
def sort_inline(d):
    n=len(d)
    for i in range (0,n):
        #check=False
        for j in range (0,n-i-1):
            if d[j]>d[j+1]: d[j],d[j+1]=d[j+1],d[j];check=True
        #if not check: break
    return d
