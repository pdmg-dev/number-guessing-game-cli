import random
from config import MIN_VAL, MAX_VAL

def generate_number():
  return random.randint(MIN_VAL, MAX_VAL)

def check_guess(guess, secret):
  if guess == secret:
    return "correct"
  elif guess < secret:
    return "low"
  else:
    return "high"