import pylab
import random

def montyChoose(guessDoor, prizeDoors):
    goats = []
    for i in [1,2,3,4]:
        if i not in prizeDoors and i != guessDoor:
            goats.append(i)
    return random.choice(goats)
    
    #if 1 != guessDoor and 1 not in prizeDoors:
    #    return 1
    #if 2 != guessDoor and 2 not in prizeDoors:
    #    return 2
    #if 3 != guessDoor and 3 not in prizeDoors:
    #    return 3
    #else:
    #    return 4
#def randomChoose(guessDoor, prizeDoor):
#    if guessDoor == 1:
#        return random.choice([2,3])
#    if guessDoor == 2:
#        return random.choice([1,3])
#    return random.choice([1,2])
    
def simMontyHall(numTrials, chooseFcn):
    stickWins, switchWins, noWin = (0, 0, 0)
    doors = [1,2,3,4]
    guessChoices = [1,2,3,4]
    playerStick = True
    for t in range(numTrials):
        prizeDoors = random.sample([1, 2, 3, 4],2)
        guess = random.choice(doors)
        toOpen = chooseFcn(guess, prizeDoors)
        if guess in prizeDoors:
            stickWins += 1
        
        newchoices = []
        for i in doors:
            if i != guess and i != toOpen:
                newchoices.append(i)
        guess = random.choice(newchoices)
        if guess in prizeDoors:
            switchWins += 1
        
            
        #print "Player guess " + str(guess)
        #print "Monty open " + str(toOpen)
        #print "Prize door choices" + str(prizeDoors)
        
        
        

            
        #if toOpen in prizeDoors:
        #    noWin += 1
        #elif guess in prizeDoors:
        #    stickWins += 1
        #else:
        #    switchWins += 1
    return (stickWins, switchWins)

def displayMHSim(simResults, title):
    stickWins, switchWins = simResults
    pylab.pie([stickWins, switchWins],
              colors = ['r', 'c'],
              labels = ['stick', 'change'],
              autopct = '%.2f%%')
    pylab.title(title)

simResults = simMontyHall(100000, montyChoose)
displayMHSim(simResults, 'Monty Chooses a Door')
pylab.figure()
#simResults = simMontyHall(100000, randomChoose)
#displayMHSim(simResults, 'Door Chosen at Random')
pylab.show()
