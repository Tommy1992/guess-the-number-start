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
from art import logo
guesses_left = 10


def set_diff():
  """ Asks user for difficulty and sets the guesses left."""
  diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if diff == "easy":
    guesses_left = 10
    print (f"You have {guesses_left} guesses left.\n")
  elif diff == "hard":
    guesses_left = 5
    print (f"You have {guesses_left} guesses left.\n")

current_guess = 0

def check_answer(guesses_left, current_guess, num):
  while guesses_left > 0:
    current_guess = input("Make a guess: ")
    if int(current_guess) > num:
      print (f"Too high.")
    elif int(current_guess) < num:
      print (f"Too low.")
    elif int(current_guess) == num:
      print ("You got it! The answer was " + str(num) + ".")
      return
    guesses_left -= 1
    if guesses_left == 0:
      print("You've run out of guesses, you lose.")
      return
    print (f"You have {guesses_left} guesses left.")


def game():
  print (logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  num = rnd.randint(1,100)
  print(f"Pssst, the correct answer is {num}")
  set_diff()
  check_answer(guesses_left, current_guess, num)

game()
