
def countingValleys(n, s):
    """
    Gray is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last
    hike he took exactly n steps. For every step he took, he noted if it was an uphill, U, or a downhill, D step. 
    Gray hikes start and end at sea level and each step up or down represents a 1 unit change in altitude. We define the following
    terms:

    A mountain is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step 
    up to sea level. 

    Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through. 

    For example, if Gary's path is s = [DDUUUUDD], he first enters a valley 2 units deep. Then he climbs out an up onto a 
    mountain 2 units high. Finally, he returns to sea level and ends his hike. 

    Function Description

    complete the countingValleys function. It must return an integer that denotes the number of valleys Gary traversed. 

    countingValleys has the following parameters(s):
    n: the number of steps Gary takes 
    s: a string describing his path 

    Input Format 

    The first line contains an integer n, the number of steps in Gary's hike. 
    The second line contains a single string, s, of n characters that describe his path. 

    """
    #track levels with a variable starting with 0 
    levels = 0
    # This will be used to gadge where we are < 0
    belowSeaLevel = False
    #this will be used to gadge where we are > 0 
    aboveSeaLevel = False
    #this will be used to keep track of current place without conditionals 
    #for if the step is 'U' do this or if the step is 'D' do that. 
    steps = {'U': 1, 'D': -1}
    #starts off at zero because sea level will be considered 0 and we start and end at sea level.
    current = 0
    #set previousBelowSeaLevel = to false will be used to check previous conditions against current
    previousBelowSeaLevel = False
    #set previousAboveSeaLevel = to false will be used to check previous conditions against current 
    previousAboveSeaLevel = False
    #iterate over the s array/list may want to have access to indexs. 
    for index, step in enumerate(s):
        #add the step value from steps to the current variable. 
        current += steps[step]
        #set previous variables to the current. 
        previousAboveSeaLevel = aboveSeaLevel
        previousBelowSeaLevel = belowSeaLevel
        #check if current is above or below seaLevel which is 0

        #we will only perform this action if belowSeaLevel is not already True
        #This will cut number of operations. 
        if current < 0 and not belowSeaLevel:
            #set belowSeaLevel to True and above to False
            belowSeaLevel = True
            aboveSeaLevel = False

        #we will only perform this action if aboveSeaLevel is not already True
        elif current > 0 and not aboveSeaLevel:
            #set aboveSeaLevel to True and below to False
            aboveSeaLevel = True
            belowSeaLevel = False
    
        #else leave everything alone. while 0 is not above or below we keep it the same for later use 
        #when it is desired to check where we have been. 
        
        #check if index is greater than 0 
        if index > 0:
          #new conditional check if the previousBelowSeaLevel is true and current is back to sealevel 0 
          if previousBelowSeaLevel and current == 0:
            levels += 1
          # elif previousAboveSeaLevel and belowSeaLevel:
          #   levels += 1
    #end of for loop

    #return levels
    return levels

        
        




# end of countingValleys function

test = ['U','D','D','D','U','D','U','U']
n = len(test)
print(countingValleys(n,test))

test2 = ['D','D','U','U','U','U','D','D']
n = len(test)
print(countingValleys(n,test2))

test3 = ['D','D','U','U','D','D','U','D','U','U','U','D']
n = len(test3)
print(countingValleys(n,test3))

