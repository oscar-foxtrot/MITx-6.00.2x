def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    res = []
    minlen = 0
    for i in cows:
        if cows[i] <= limit:
            res.append([i])
            minlen += 1 # Initialized minlen and res
            
    for tmppart in get_partitions(cows):
        overflow = False
        for ilist in tmppart:
            curtripweight = 0
            for j in ilist:
                curtripweight += cows[j]
            if curtripweight > limit:
                overflow = True
                break 
            
        if not overflow:
            lentmp = len(tmppart)
            if lentmp <= minlen:
                res = tmppart
                minlen = lentmp
                
    return res
