# Number Guessing Game (CLI)

A simple Python CLI number guessing game where players try to guess a randomly generated number between 1 and 100. Choose your difficulty, beat the timer, and set high scores!

## Features

- Difficulty levels: Easy, Medium, Hard
- Adjustable number of chances per level
- Real-time performance timer
- Persistent high score tracking (stored in JSON)
- Modular and readable code structure

## How to Run

```bash
python main.py

```

## Requirements

Python 3.7+

## Game Rules

- The game randomly picks a number between 1–100.
- You pick a level, which sets your allowed number of guesses.
- After each guess, the game tells you whether to go higher or lower.
- If you guess correctly within the limit, your time and attempts are logged.
- If your score beats the previous high score, it gets saved!

## Project Structure

```bash

├── main.py
├── config.py
├── data/
│   └── highscores.json
├── game/
│   ├── engine.py
│   ├── logic.py
│   └── score.py
├── ui/
│   ├── display.py
│   └── input_handler.py
├── utils/
│   ├── timer.py
│   └── validator.py
├── .gitignore
└── README.md

```

## High Score Data

High scores are stored in data/highscores.json in this format:

```bash
{
  "easy": { "tries": 7, "duration": 15.7 },
  "medium": { "tries": 4, "duration": 13.38 },
  "hard": { "tries": 4, "duration": 7.42 }
}

```

## License

This project is open-source. Feel free to fork, extend, and improve.

## Project Source

This project was developed following the [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) specification from [roadmap.sh](https://roadmap.sh/).
