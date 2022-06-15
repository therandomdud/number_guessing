from random import randint, random, uniform


Low = int(input('the smallest possible number:'))
High = int(input('the largest possible number:'))
NumToGuess = randint(Low,High)


runG = True

while runG == True:
 x = int(input('witch number is it:'))
 if x > NumToGuess:
  print('lower')
 elif x < NumToGuess:
  print('higher')
 elif x == NumToGuess:
  print('you won')
  runG = False    
   #du bist gay 
    

        
