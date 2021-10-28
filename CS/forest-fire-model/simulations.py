# We will use the forest_fire module.
# There is the function simulate_forest_fire
# that we can use to simulated our model
from forest_fire import simulate_forest_fire
import random

# Comments (*NOT* requested to do this for the project #3)
# In the current code, we do simple statistics; computing only mean value, and quartiles
# https://en.wikipedia.org/wiki/Quartile
# It would be much better to do more "advanced" statistics (like in Project 2 about sorting)
# At least, one could use confidence interval (or similar) to evaluate accuracy of the results!
# Or to use variance, or ...
# To keep it simple, I decided to omit it in this project!

def multiple_simulations(nb_simus, size, b, p, max_time, diag_neigh, seed=None):
    """
    This function allows to repeat nb_simus simulations with the same parameters.
    Return simple statistics about the simulations; for three metrics:
    (mean value, Q1, median=Q2, Q3)
    
    Check https://en.wikipedia.org/wiki/Quartile for Q1, Q2, Q3
    Check function simulate_forest_fire for the explanations of parameters.
    """

    if seed is None:
        random.seed(0)
    else:
        random.seed(seed)
    
    # Variables to store the list of results
    # Note: that we do not need to track both burnt and alive trees
    #       it is easy to deduce one from the other!
    nb_burnt_trees = []
    nb_alive_trees = []
    nb_timesteps = []
    
    for _ in range(nb_simus):
        nb_b, nb_a, nb_t = simulate_forest_fire(size, b, p, max_time, diag_neigh)
        nb_burnt_trees.append(nb_b)
        nb_alive_trees.append(nb_a)
        nb_timesteps.append(nb_t)
    
    nb_burnt_trees.sort()
    nb_alive_trees.sort()
    nb_timesteps.sort()
    
    # For all three metrics, return a tuple containing (mean, Q1, Q2, Q3)
    # In total, the returning value is of the shape: (a,b,c,d, e,f,g,h), i,j,k,l)
    # Note: In python, the value returned by a function can be very complex !
    Q1 = nb_simus // 4
    Q2 = nb_simus // 2
    Q3 = 3*nb_simus // 4
    return sum(nb_burnt_trees)/nb_simus, nb_burnt_trees[Q1], nb_burnt_trees[Q2], nb_burnt_trees[Q3], \
           sum(nb_alive_trees)/nb_simus, nb_alive_trees[Q1], nb_alive_trees[Q2], nb_alive_trees[Q3], \
           sum(nb_timesteps)/nb_simus, nb_timesteps[Q1], nb_timesteps[Q2], nb_timesteps[Q3]
       
    #return [sum(nb_burnt_trees)/nb_simus]


def variable_proba_propagation(nb_simus, size, b, list_of_p, max_time, diag_neigh, num, seed=None):
    """
    This function executes simulations with variable probability p of fire propagation
    One can see the effect of p on the number of burnt trees
    Note: This function *only* display (ie. print) results in the terminal
          The function does not return anything
    """
    s="dummy.txt"
    #s="variable_proba_propagation_for_time"+num+".txt"
    print("Now: open file "+s)
    f=open(s,"w")
    for p in list_of_p:
        print("Now: writing file "+s+" for ",p)
        #print(p, multiple_simulations(nb_simus, size, b, p, max_time, diag_neigh, seed))
        f.write(str(b));f.write(" ")
        f.write(str(p));f.write(" ")
        for x in multiple_simulations(nb_simus, size, b, p, max_time, diag_neigh, seed):
            f.write(str(x));f.write(" ")
        f.write("\n")
    f.close()
    print("Now: close file "+s)
# Example of usage of variable_proba_propagation:
# variable_proba_propagation(1000, 50, 5, list(x/10 for x in range(11)), 10000, False)
# May take 1-2min to complete with these parameters



def variable_burning_duration(nb_simus, size, list_of_b, p, max_time, diag_neigh, seed=None):
    """
    This function executes simulations with variable probability p of fire propagation
    One can see the effect of p on the duration of burning
    Note: This function *only* display (ie. print) results in the terminal
          The function does not return anything
    """
    for b in list_of_b:
        print(b, multiple_simulations(nb_simus, size, b, p, max_time, diag_neigh, seed))
# Example of usage of variable_burning_duration:
# variable_burning_duration(1000, 50, list(range(1,12)), 0.1, 10000, False)
# May take 1-2min to complete with these parameters


    
    
    