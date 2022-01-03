#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
""""
toDo list:
put ASCII art logo file into replit
imports:
import logo from art
import random as rnd
global variable:
guesses_left (changes when mdoe is chosen and when an attempt is made)

Code:
randomize the number
check for diff chosen
function: while guesses_left > 0:
check if guess is correct or too high/low and print:
  attemps left, too high/low
"""

import random as rnd

num = rnd.randint(1,100)

diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
if diff == "easy":
  guesses_left = 10
  print (f"You have {guesses_left} guesses left.\n")
elif diff == "hard":
  guesses_left = 5
  print (f"You have {guesses_left} guesses left.\n")

while guesses_left > 0:
  if guesses_left == 0:
    print ("You've run out of guesses, you lose.")
  guesses_left -= 1
  current_guess = input("Make a guess: ")
  if int(current_guess) > num:
    print (f"Too high.\nYou have {guesses_left} guesses left.\nGuess again.")
  elif int(current_guess) < num:
    print (f"Too low.\nYou have {guesses_left} guesses left.\nGuess again.")
  elif int(current_guess) == num:
    print ("You got it! The answer was " + str(num) + ".")
    guesses_left = 0