import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

from sort_core import create_random_array, is_sorted
from timed import timed


import selection
import bubblesort
import insertion
import mergesort
import quicksort
import radixsort

ALGORITHMS = [
        #Algorithm name,   Color,    Algorithm function
        ("Selection sort",  "Blue",   selection.sort ),
        ("Insertion sort",  "Magenta",   insertion.sort ),
        ("Bubble sort",     "Green",  bubblesort.sort ),
        ("Quicksort",       "Orange", quicksort.sort ),
        ("Merge sort",      "Red",    mergesort.sort ),
        ("Builtin sort",    "Black",  sorted ),
        ("Radix sort",    "Cyan",  radixsort.sort ),
]

REPETITIONS  = 10

TEST_SIZES  = [10,100,500,1000,2000,5000]
#TEST_SIZES  = [100,1000,5000,7500]
TEST_ARRAYS = [
    ( size, [ create_random_array(size) for i in range(REPETITIONS) ] )
        for size in TEST_SIZES
]


def mean_ci(data, conf_level=0.95, two_sided=True):
    if two_sided:
        conf_level =  1 - (1-conf_level)/2
    n    = data.size
    mean = np.mean(data)
    df   = n-1
    sdv  = np.std(data)
    ci   = stats.t.ppf(conf_level, df) * sdv / np.sqrt(n)
    return (mean, ci)


def timed_sort(sort_fct, array):
    a = sort_fct(array)
    if not is_sorted(a):
        print("Offending input: ", a)
    assert( is_sorted(a) )
    time = timed(lambda: sort_fct(array))
    return time * 1000 # as milliseconds


# gather execution data
data = [ {} for _ in ALGORITHMS ]

for k, (name, col, sort) in enumerate(ALGORITHMS):
    print("- ", name)
    means = np.empty(len(TEST_ARRAYS))
    lcis  = np.empty(len(TEST_ARRAYS))
    hcis  = np.empty(len(TEST_ARRAYS))
    
    for i, (size, arrays) in enumerate(TEST_ARRAYS):
        print(f"  {size},", end="", flush=True)
        times = np.fromiter((timed_sort(sort, array) for array in arrays), float)
        mean, ci = mean_ci(times)
        means[i] = mean
        lcis[i] = mean-ci
        hcis[i] = mean+ci
        print(mean)
    
    data[k]['name']  = name
    data[k]['color'] = col
    data[k]['means'] = means
    data[k]['lcis'] = lcis
    data[k]['hcis'] = hcis
    print("...done")


# plot the data
fig, ax = plt.subplots()

for entry in data:
    ax.fill_between(TEST_SIZES, entry['hcis'], entry['lcis'], color=entry['color'], alpha=.25)
    ax.plot(TEST_SIZES, entry['means'], color=entry['color'], label=entry['name'])
    
ax.set_xscale("log", nonposx='clip')
ax.set_yscale("log", nonposy='clip')
ax.set_ylim(ymin=0.001)  
ax.set(xlabel='array size', ylabel='running time [ms]',
       title='Running time of sorting algorithms')
ax.legend()
ax.grid()
fig.savefig("sort_comparison_big_opt3.pdf")
plt.show()

