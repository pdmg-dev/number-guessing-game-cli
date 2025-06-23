from game.engine import start_new_game
from ui.display import welcome_message, goodbye_message
from ui.input_handler import ask_play_again

def game_loop():
  welcome_message()
  while True:
    start_new_game()
    if not ask_play_again():
      break
  goodbye_message()

if __name__ == "__main__":
  game_loop()