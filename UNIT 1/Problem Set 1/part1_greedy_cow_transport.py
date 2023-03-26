def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowlist = sorted(cows, key=cows.get, reverse=True)
    try:
        while cows[cowlist[0]] > limit:
            del(cowlist[0])
    except IndexError:
        return []
  
    res = []
    
    while cowlist:
        avail = limit
        curtrip = []
        
        i = 0
        try:
            while True:
                while cows[cowlist[i]] > avail:
                    i += 1
                curtrip.append(cowlist[i])
                avail -= cows[cowlist[i]]
                del(cowlist[i])  
        except IndexError:
            res.append(curtrip)
        
    return res
