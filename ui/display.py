def welcome_message():
  print(
    "\nGuess the Number!\n" \
    "\nI'm thinking of a number between 1-100.\n" \
    "Do you think you can figure it out?" \
  )

def level_feedback(level):
  from config import LEVELS
  if level == "1":
    print(f"\nEasy? Okay, have fun. You've got {LEVELS[level][1]} tries.")
  elif level == "2":
    print(f"\nMedium, huh? Let's see what you've got — {LEVELS[level][1]} guesses.")
  else:
    print(f"\nHard? Oh, built different? You get {LEVELS[level][1]} tries.")
  print("Guess the number!")

def guess_feedback(result, tries, chances):
  if chances-tries != 0:
    if result == "correct":
      print("\nCongrats! You guessed the number.")
    elif result == "low":
      print("\nHigher. Try again.")
    elif result == "high":
      print("\nLower. Try again.")
    else:
      return
    
def win_message(tries, duration):
  print(f"You won in just {tries} tries within {duration:.2f} seconds.\n")
  
def lose_message(secret):
  print(f"\nSorry, out of tries. The number was {secret}.")

def goodbye_message():
  print("\nThanks for playing. Bye.\n")