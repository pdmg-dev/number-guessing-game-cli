from ui.display import level_feedback
from utils.validator import is_valid
from config import LEVELS, MIN_VAL, MAX_VAL

def select_level():
  while True:
    print("\nSelect level: [1] Easy [2] Medium [3] Hard")
    level = input("> ")
    if is_valid(level=level):
      level_feedback(level)
      return LEVELS[level][0], LEVELS[level][1]
    print("\nJust pick a level from 1-3.")

def get_guess():
  while True:
    guess = input("> ")
    if is_valid(guess=guess):
      return int(guess)
    print(f"\nJust pick a number from {MIN_VAL}-{MAX_VAL}.")

def ask_play_again():
  while True:
    print("Wanna play again? [Y/N]")
    answer = input("> ").strip().lower()
    if answer in ["y", "yes"]:
      return True
    elif answer in ["n", "no"]:
      return False
    print("\nJust answer yes or no.")