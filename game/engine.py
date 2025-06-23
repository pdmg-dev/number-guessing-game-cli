from game.logic import generate_number, check_guess
from game.score import update_high_scores
from ui.input_handler import select_level, get_guess
from ui.display import guess_feedback, win_message, lose_message
from utils.timer import start_timer, stop_timer

def start_new_game():
  level, chances = select_level()
  secret = generate_number()
  tries = 0
  start_timer()
  while tries < chances:
    guess = get_guess()
    tries += 1
    result = check_guess(guess, secret)
    guess_feedback(result, tries, chances)
    if result == "correct":
      duration = stop_timer()
      win_message(tries, duration)
      update_high_scores(level, tries, duration)
      return
  lose_message(secret)