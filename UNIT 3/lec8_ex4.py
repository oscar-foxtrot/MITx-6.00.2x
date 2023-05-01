import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    successes = 0
    bucket = [0 for x in range(3)] + [1 for x in range(3)] # 1 for green, 0 for red
    for i in range(numTrials):
        successes += runSim(bucket)  
    return successes / numTrials
        
def runSim(bucket):
   bucket = bucket.copy()
   first = random.choice(bucket)
   bucket.remove(first)
   for i in range(2):
       ball = random.choice(bucket)
       bucket.remove(ball)
       if ball != first:
           return False         
   return True
