# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    ## Parameters stipulated in PSET4
    numViruses  = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False} 
    mutProb = 0.005

    def Trial(insertionPoint):
    # creating a list of virus instances
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

        # creating the patient
        patient = TreatedPatient(viruses, maxPop)

        virusPops = []
        resPops = []
        
        # combining both loops into a single 450 step loop
        for i in range(450):
            if i == insertionPoint:
                patient.addPrescription('guttagonol')
            try:
                virusPops.append(patient.update())
            except:
                pass
            try:
                resPops.append(patient.getResistPop(['guttagonol']))
            except:
                resPops.append(0.0)
        return virusPops, resPops
    
    # Running the trials
    # This is incorrect
    insertionPoints = [300, 150, 75, 0]
    for insertionPoint in insertionPoints:
        virusTrials = []
        resTrials = []
        for i in range(numTrials):
            virusAdd, resAdd = Trial(insertionPoint)
            virusTrials.append(virusAdd)
            print "Numtrials: " + str(numTrials)
            print "Virus Trials: " + str(virusTrials)
            resTrials.append(resAdd)
        virusAvg = [float(sum(col))/len(col) for col in zip(*virusTrials)]
        resAvg = [float(sum(col))/len(col) for col in zip(*resTrials)]
    
        # plotting graphs for each trial. This will need to change to histogram
        pylab.plot(range(len(virusAvg)), virusAvg, label = "Virus Average")
        pylab.plot(range(len(resAvg)), resAvg, label = "Resistant Virus Average")
        pylab.title("Resistant Virus Simulation. Insertion point: " + str(insertionPoint))
        pylab.xlabel("time step")
        pylab.ylabel("# viruses")
        pylab.legend()
        pylab.show()

simulationDelayedTreatment(2)



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
