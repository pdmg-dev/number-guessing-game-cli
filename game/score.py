import os
import json

HIGH_SCORES = "data/highscores.json"
DEFAULT_SCORES = {"easy": None, "medium": None, "hard": None}

def load_scores():
  if not os.path.exists(HIGH_SCORES):
    return DEFAULT_SCORES.copy()
  try:
    with open(HIGH_SCORES, "r") as f:
      data = json.load(f)
      return {key: data.get(key, None) for key in DEFAULT_SCORES}
  except json.decoder.JSONDecodeError as e:
    return {}
  
def save_score(scores):
  os.makedirs(os.path.dirname(HIGH_SCORES), exist_ok=True)
  with open(HIGH_SCORES, "w") as f:
    return json.dump(scores, f, indent=2)
  
def update_high_scores(level, tries, duration):
  scores = load_scores()
  current_best = scores.get(level)

  if current_best is None or (tries < current_best["tries"]) or (tries == current_best["tries"] and duration < current_best["duration"]):
    
    scores[level] = {
      "tries": tries,
      "duration": round(duration, 2)
      }
    
    print("New high score!")
    save_score(scores)