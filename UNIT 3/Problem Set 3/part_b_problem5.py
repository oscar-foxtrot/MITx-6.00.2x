#
# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    ntimesteps0 = 150 # Administering a drug after "ntimesteps0" timesteps
    ntimesteps1 = 150
    avpop = [0 for x in range(ntimesteps0 + ntimesteps1)]
    avpopgut = avpop.copy()
    pylab.figure(0)
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, \
        mutProb) for x in range(numViruses)]
    
    for i in range(numTrials):
        curpat = TreatedPatient(viruses, maxPop)
        for j in range(ntimesteps0):
            curpat.update()
            avpop[j] += curpat.getTotalPop()
            avpopgut[j] += curpat.getResistPop(['guttagonol'])
            
        curpat.addPrescription('guttagonol') # Administering a drug
        
        for j in range(ntimesteps0, ntimesteps0 + ntimesteps1):
            curpat.update()
            avpop[j] += curpat.getTotalPop()
            avpopgut[j] += curpat.getResistPop(['guttagonol'])
            
    for j in range(ntimesteps0 + ntimesteps1):
        avpop[j] /= numTrials
        avpopgut[j] /= numTrials
    
    pylab.plot(avpop, label = "ResistantVirus", color = 'r')
    pylab.plot(avpopgut, label = "Guttagonol-ResistantVirus", color = 'g')
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()
