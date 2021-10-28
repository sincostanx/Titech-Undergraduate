from time import time

#
# measures the time (in seconds) taken to compute a function passed as argument
#
# Ex: time = timed (lambda: do_something(), k=5)
#
def timed(fct, k=1):
    start = time()
    for i in range(k):
        fct()
    stop = time()
    return (stop - start) / k
