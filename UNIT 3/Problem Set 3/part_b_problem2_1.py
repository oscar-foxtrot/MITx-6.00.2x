#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    ntimesteps = 300
    avpop = [0 for x in range(ntimesteps)]
    pylab.figure(0)
    viruses = [SimpleVirus(maxBirthProb, clearProb) for x in range(numViruses)]
    
    for i in range(numTrials):
        curpat = Patient(viruses, maxPop)
        for j in range(ntimesteps):
            curpat.update()
            avpop[j] += curpat.getTotalPop()
    
    for j in range(ntimesteps):
        avpop[j] /= numTrials
    
    pylab.plot(avpop, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()
