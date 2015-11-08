import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    wins = 0.0
    for i in range(numTrials):
        balls = ["red", "red", "red", "green", "green", "green"]
        choices = []
        for i in range(3):
            choice = random.choice(balls)
            choices.append(choice)
            balls.remove(choice)
        if all(x == choices[0] for x in choices):
            wins += 1
    return wins/float(numTrials)
        
