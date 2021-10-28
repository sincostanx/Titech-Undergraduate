# This file can be used to run simulations and generate data
# You need to choose "good" parameters and explain your choices
# I give two examples

from simulations import variable_proba_propagation, variable_burning_duration


# Example of usage of variable_proba_propagation:
for time_burn_down in range(1,2):
    variable_proba_propagation(1000, 50, time_burn_down, list(x/100 for x in range(101)), 10000, False,str(time_burn_down))
    print()
# May take 1-2min to complete with these parameters
# list(x/10 for x in range(11)) creates the list [0, 0.1, 0.2, ..., 1.0]

# Example of usage of variable_burning_duration:
# variable_burning_duration(1000, 50, list(range(1,12)), 0.1, 10000, False)
# May take 1-2min to complete with these parameters