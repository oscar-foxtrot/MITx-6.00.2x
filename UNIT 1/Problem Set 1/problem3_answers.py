# Part 3-1
# Now that you have run your benchmarks, which algorithm runs faster?

# --> ANSWER: The Greedy Transport Algorithm

# Explanation: Greedy takes O(n^2) to run in the worst case while
# Brute-force takes O(exp(n)) time to run in all cases (worst, average, best), which is significanly slower

#-----------------------------------------
#-----------------------------------------

# Part 3-2
# Consider the properties of the GREEDY algorithm. Will it return the optimal solution?

# --> ANSWER: It could, but it depends on the data, not always.

# Explanation: Suppose all the elements of the set have the same values (cows with the same weights).
# In this case, of course, greedy will return the optimal solution
# But if we have the following set of cows:
# {'Maggie':3, 'Herman':7, 'Betsy':9, 'Oreo':6, 'Moo Moo':3, 'Milkshake':2, 'Millie':5, 'Lola':2, 'Florence':2, 'Henrietta':9}
# (the set given in the task)
# Then greedy algorithm will return a solution with 6 trips while the optimal is 5 trips

#-----------------------------------------
#-----------------------------------------

# Part 3-3
# Consider the properties of the BRUTE FORCE algorithm. Will it return the optimal solution?

# --> ANSWER: Yes, all the time

# Explanation: Brute-force algorithm considers every possible soultion, thus it is able to determine the best one




# The algorithm used for comparison

def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
        greedy_cow_transport(cows, limit)
    end = time.time()
    print('greedy took ' + str(end - start) + ' seconds to run')
    
    start = time.time()
        brute_force_cow_transport(cows, limit)
    end = time.time()
    print('brute-force took ' + str(end - start) + ' seconds to run')
