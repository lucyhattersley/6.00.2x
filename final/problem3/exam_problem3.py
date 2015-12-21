import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    rabbits = CURRENTRABBITPOP
    for rabbit in range(rabbits):
        if random.random() < (1.0 - (float(CURRENTRABBITPOP) / float(MAXRABBITPOP))):
            CURRENTRABBITPOP += 1            

def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    foxes = CURRENTFOXPOP
    for fox in range(foxes):
        foxEats = False
        if CURRENTRABBITPOP > 10 and random.random() < (float(CURRENTRABBITPOP) / float(MAXRABBITPOP)):
            foxEats = True

        if foxEats:
            CURRENTRABBITPOP -= 1
            if random.randint(1,4) == 1: # fox breeds
                CURRENTFOXPOP += 1
        else:
            if CURRENTFOXPOP > 10 and random.randint(1,10) ==1 :
                CURRENTFOXPOP -= 1 # fox dies

def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    # TO DO
    timeStep = 0
    rabbit_populations = []
    fox_populations = []
    while timeStep < numSteps:
        rabbitGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        
        foxGrowth()
        fox_populations.append(CURRENTFOXPOP)
        
        timeStep += 1
    return (rabbit_populations, fox_populations)

pops = runSimulation(200)
# print pops
# pylab.plot(pops[0]) # rabbit_populations
# pylab.plot(pops[1]) # fox_populations
# pylab.show()

coeff = pylab.polyfit(range(len(pops[0])), pops[0], 2)
pylab.plot(pylab.polyval(coeff, range(len(pops[0]))))

coeff = pylab.polyfit(range(len(pops[1])), pops[1], 2)
pylab.plot(pylab.polyval(coeff, range(len(pops[1]))))


pylab.show()
