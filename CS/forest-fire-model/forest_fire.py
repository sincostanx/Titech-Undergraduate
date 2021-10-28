import random


def simulate_forest_fire(size, b, p, max_time, diag_neigh=False, seed=None):
    """
    Simulate the propagation of fire in a squared grid forest
    Returns a triplet of integers:
        - the number of burnt trees
        - the number of non-burnt trees
        - Number of timesteps taken by simulation
    
    Parameters are:
        - size: length of the side of the squared forest
                There are size*size trees in this forest
        - b: Burning time of a tree
             Each tree will burn for b unit of time
             During this period the neighboring trees may catch fire
        - p: probability that a neighbor catches fire
             Note: if a given non-yet-burning tree has multiple burning neighbors,
                   each of these neighbors has a 'chance' of propagating fire
        - max_time: Simulation will stop after max_time unit of times
                    even if there are still some burning trees
        - diag_neigh: Boolean to indicate whether fire can also propagate
                      via diagonal neighbors. Default is False, which means
                      that fire propagates only via the four cardinal directions
        - seed: Can be used to fixed the seed of the random generator
    """
    
    # If a seed is given, use it to initialize the (pseudo)random generator
    if seed is not None:
        random.seed(seed)
    
    # Initialize a forest: matrix of dimension size*size
    # Initially all trees are represented with value True (=alive tree)
    forest = [[True]*size for _ in range(size)]

    # Fire start with the tree in the center (approximately)
    mid = size//2
    forest[mid][mid] = False
    nb_burnt_trees = 1
    burning_trees = [ [(mid,mid)] ] + [ [] for _ in range(b-1)]
    # burning_trees is a list of b list:
    #   burning_trees[0] contains the list of trees that just started to burn
    #   burning_trees[1] contains the list of trees that already burnt for 1 timestep
    #   burning_trees[2] contains the list of trees that already burnt for 2 timesteps
    #   ...
    #   burning_trees[b-1] contains the list of trees that already burnt for b-1 timesteps
    #   Each tree in burning_trees[b-1] will be completely burnt at the next timestep
    #   and will not be able to "transmit" fire to its neighboring trees
    
    
    # Initialize some variables used in the simulation
    # Simulation stops when either there is no more tree still burning
    # or when reaching t=max_time (timeout given in parameter)
    t = 0
    still_burning = True
    
    # Main loop to simulate one timestep of the 
    while t < max_time and still_burning:
        # We need to iterate over *all* burning trees
        # For each burning tree, its neighbor may catch fire (if not yet burning/burnt)
        
        # Let's keep track of trees that catch fire in this round
        # this list is initially empty
        new_burning_trees = []
        
        # Update simulation variables
        # still_burning is reset to False
        # If there is still a tree burning, we will switch it back to True
        t += 1
        still_burning = False
        
        for L in burning_trees: # Remember burning_trees is a list of list
            for (x,y) in L:    # Let's get the coordinate of burning trees
                still_burning = True  # If L is not empty, it means that (at least) one tree is still burning
                
                # Let's check all neighbors of this tree
                # We need to be careful not being out of the forest!
                if x > 0: # Left neighbor
                    if forest[x-1][y] == True:  # Check that the tree is not yet burning (==True is not necessary)
                        if random.random() < p: # Check if the neighboring tree "successfully" catches fire
                            # Tree is catching fire !
                            forest[x-1][y] = False  # Tree is in fire now
                            nb_burnt_trees += 1     # Update the number of burnt trees
                            new_burning_trees.append( (x-1,y) )
                
                # Right neighbor, but in a condensed writing:
                if x < size-1 and forest[x+1][y] and random.random() < p:
                    forest[x+1][y] = False
                    nb_burnt_trees += 1
                    new_burning_trees.append( (x+1,y) )
                
                # Above neighbor
                if y > 0 and forest[x][y-1] and random.random() < p:
                    forest[x][y-1] = False
                    nb_burnt_trees += 1
                    new_burning_trees.append( (x,y-1) )
                
                # Below neighbor
                if y < size-1 and forest[x][y+1] and random.random() < p:
                    forest[x][y+1] = False
                    nb_burnt_trees += 1
                    new_burning_trees.append( (x,y+1) )
                
                if diag_neigh: # Fire can also propagate in diagonal
                    # Above-left
                    if x > 0 and y > 0 and forest[x-1][y-1] and random.random() < p:
                        forest[x-1][y-1] = False
                        nb_burnt_trees += 1
                        new_burning_trees.append( (x-1,y-1) )
                    # Below-left
                    if x > 0 and y < size-1 and forest[x-1][y+1] and random.random() < p:
                        forest[x-1][y+1] = False
                        nb_burnt_trees += 1
                        new_burning_trees.append( (x-1,y+1) )
                    # Above-right
                    if x < size-1 and y > 0 and forest[x+1][y-1] and random.random() < p:
                        forest[x+1][y-1] = False
                        nb_burnt_trees += 1
                        new_burning_trees.append( (x+1,y-1) )
                    # Below-right
                    if x < size-1 and y < size-1 and forest[x+1][y+1] and random.random() < p:
                        forest[x+1][y+1] = False
                        nb_burnt_trees += 1
                        new_burning_trees.append( (x+1,y+1) )
                    
        # Update the list (of lists) of burning trees
        # Remove the oldest burning trees that finished burning
        # and add the new burning trees
        # Note: some_list[:-1] returns the list without the last element
        burning_trees = [new_burning_trees] + burning_trees[:-1]
    
    #print(nb_burnt_trees, n*n-nb_burnt_trees)
    return nb_burnt_trees, size*size-nb_burnt_trees, t

        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    