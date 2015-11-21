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

        # Running 450 steps (adding drug at insertionPoint)
        # Returns the final drug count
        for i in range(450):
            if i == insertionPoint:
                patient.addPrescription('guttagonol')
            try:
                patient.update()
            except:
                pass
        return patient.getTotalPop()
    
    # Running the trials
    insertionPoints = [300, 150, 75, 0]
    for insertionPoint in insertionPoints:

        populations = []

        for trial in range(numTrials):
            trialResults = []
            for t in range(trial):
                trialResults.append(Trial(insertionPoint))
            if sum(trialResults) > 0:
                populations.append(sum(trialResults) / len(trialResults))
            print populations

        pylab.hist(populations)
        pylab.show()

simulationDelayedTreatment(10)



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
