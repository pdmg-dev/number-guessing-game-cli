from config import LEVELS

def is_valid(level=None, guess=None):
  if level is not None:
    return level in LEVELS
  if guess is not None:
    return guess.isdigit() and 1 <= int(guess) <= 100
  
