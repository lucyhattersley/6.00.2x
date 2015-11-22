import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    count = 0.0

    for trial in range(numTrials):
        bucket = ['red', 'red', 'red', 'red', 'green', 'green', 'green', 'green']
        choices = []
        
        for i in range(3):
            choice = random.choice(bucket)
            choices.append(choice)
            bucket.remove(choice)
        
        if all(x == choices[0] for x in choices):
            count += 1
        
    return count / numTrials

print drawing_without_replacement_sim(100000)