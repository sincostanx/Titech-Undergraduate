from random import sample


def create_random_array(n):
    if n < 0: raise ValueError("negative size")
    return sample(range(10*n), k=n)
    #return [x for x in range(0,n)]
    #return [x for x in range(n-1,-1,-1)]


def swap(array, i, j):
    # test validity
    if i >= len(array): raise IndexError(f"index i out of bounds (i={i})")
    if j >= len(array): raise IndexError(f"index j out of bounds (j={j})")
    if i == j: return 
    #
    # swap the values
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    

def is_sorted(array):
    for i in range(1,len(array)):
        if array[i-1] > array[i]: return False
    return True
