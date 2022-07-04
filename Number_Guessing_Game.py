from random import randint, random, uniform


low = int(input('the smallest possible number:'))
high = int(input('the largest possible number:'))
numtoguess = randint(Low,High)


runG = True

while runG == True:
 x = int(input('witch number is it:'))
 if x > numtoguess:
  print('lower')
 elif x < numtoguess:
  print('higher')
 elif x == numtoguess:
  print('you won')
  runG = False    
    
    

        
