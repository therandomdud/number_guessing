from random import randint, random, uniform


running = True
number_gen = False

while running:
 if not number_gen:
  low = int(input('Give me the smallest number you want!\n>'))
  high = int(input('Give me the highest number you want!\n>'))
  num_to_guess = randint(low, high)
  number_gen = True
  
 try:
  x = int(input("Guess your number!\n>"))
 except ValueError:
  continue
  
 if x > num_to_guess:
  print('The number is lower!')
 elif x < num_to_guess:
  print('The number is higher!')
 elif x == num_to_guess:
  print('You guessed your number!')
  number_gen = False
