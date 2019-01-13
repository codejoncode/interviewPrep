const countingValleys = (n, s) => {
    /* Gray is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last
      hike he took exactly n steps. For every step he took, he noted if it was an uphill, U, or a downhill, D step. 
      Gray hikes start and end at sea level and each step up or down represents a 1 unit change in altitude. We define the following
      terms:
  
      A mountain is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step 
      up to sea level. 
  
      Given Gary's sequence of up and down steps during his last hike, find and console.log the number of valleys he walked through. 
  
      For example, if Gary's path is s = [DDUUUUDD], he first enters a valley 2 units deep. Then he climbs out an up onto a 
      mountain 2 units high. Finally, he returns to sea level and ends his hike. 
  
      Function Description
  
      complete the countingValleys function. It must return an integer that denotes the number of valleys Gary traversed. 
  
      countingValleys has the following parameters(s):
      n: the number of steps Gary takes 
      s: a string describing his path 
  
      Input Format 
  
      The first line contains an integer n, the number of steps in Gary's hike. 
      The second line contains a single string, s, of n characters that describe his path. */
  
  let currentLevel = 0; 
  let valleys = 0; 

  for(let i = 0; i< s.length; i++){
    if (s[i] === 'U'){
      currentLevel += 1;
      if (currentLevel === 0){
        valleys += 1; 
      } 
    } else {
      currentLevel -= 1; 
    }
  }
  return valleys
}

const test = ['U','D','D','D','U','D','U','U']
let n = test.length
console.log(countingValleys(n,test))

const test2 = ['D','D','U','U','U','U','D','D']
n = test.length
console.log(countingValleys(n,test2))

const test3 = ['D','D','U','U','D','D','U','D','U','U','U','D']
n = test.length
console.log(countingValleys(n,test3))