# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials = 100):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    def Trial(insertionPoint = 150, numViruses = 100, maxPop = 1000, maxBirthProb = 0.1, clearProb = 0.05, resistances = {'guttagonol': False}, mutProb = 0.005):
        # creating a list of virus instances
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

        # creating the patient
        patient = TreatedPatient(viruses, maxPop)

        # update patient for insertion point steps
        for i in range(insertionPoint):
            try:
                patient.update()
            except:
                pass
        
        # add guttagonol
        patient.addPrescription('guttagonol')
        
        # update patient for another 150 steps
        for i in range(150):
            try:
                patient.update()
            except:
                pass

        # return patient populations
        if patient.getTotalPop() > 0:
            return patient.getTotalPop()
        else:
            return 0

    # insertionPoint Trial
#    insertionPoints = [300, 150, 75, 0]
#
#    for insertionPoint in insertionPoints:
#        trialResults = []
#        for trial in range(numTrials):
#            trialResults.append(Trial(insertionPoint=insertionPoint))
#        # drawing the histogram
#        pylab.hist(trialResults, bins=10)
#        pylab.title('Virus trial:  Insertion point = ' + str(insertionPoint))
#        pylab.xlabel('Total Population Values')
#        pylab.ylabel('No of trials')
#        pylab.savefig('/Users/Lucy/Desktop/trial' + str(insertionPoint) + '.pdf')
#        pylab.close()

# maxPops trial
#     maxPops = [1000, 2000, 4000, 8000, 10000]
#     for maxPop in maxPops:
#         trialResults = []
#         for trial in range(numTrials):
#             trialResults.append(Trial(maxPop=maxPop))
#         # drawing the histogram
#         pylab.hist(trialResults, bins=10)
#         pylab.title('Virus trial:  Max Pop = ' + str(maxPop))
#         pylab.xlabel('Total Population Values')
#         pylab.ylabel('No of trials')
#         pylab.savefig('/Users/Lucy/Desktop/trial' + str(maxPop) + '.pdf')
#         pylab.close()
#                      

    # maxBirthProb trial
#     maxBirthProbs = [0.1, 0.5, 0.9]
#     for maxBirthProb in maxBirthProbs:
#         trialResults = []
#         for trial in range(numTrials):
#             trialResults.append(Trial(maxBirthProb=maxBirthProb))
#         # drawing the histogram
#         pylab.hist(trialResults, bins=10)
#         pylab.title('Virus trial:  maxBirthProb = ' + str(maxBirthProb))
#         pylab.xlabel('Total Population Values')
#         pylab.ylabel('No of trials')
#         pylab.savefig('/Users/Lucy/Desktop/trial' + str(maxBirthProb) + '.pdf')
#         pylab.close()
#                      

    #  clearProb trial
#     clearProbs = [0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
#     for clearProb in clearProbs:
#         trialResults = []
#         for trial in range(numTrials):
#             trialResults.append(Trial(clearProb=clearProb))
#         # drawing the histogram
#         pylab.hist(trialResults, bins=10)
#         pylab.title('Virus trial:  clearProb = ' + str(clearProb))
#         pylab.xlabel('Total Population Values')
#         pylab.ylabel('No of trials')
#         pylab.savefig('/Users/Lucy/Desktop/trial' + str(clearProb) + '.pdf')
#         pylab.close()
    
    # Guttagonal resistance = True
    trialResults = []
    for trial in range(numTrials):
        trialResults.append(Trial(resistances = {'guttagonol': True}))
    # drawing the histogram
    pylab.hist(trialResults, bins=10)
    pylab.title('Virus trial:  guttagonol: True')
    pylab.xlabel('Total Population Values')
    pylab.ylabel('No of trials')
    pylab.savefig('/Users/Lucy/Desktop/trial_guttagonol_true.pdf')
    pylab.close()
                 
        
simulationDelayedTreatment(100)

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
