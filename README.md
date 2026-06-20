# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

Purpose of the Game
- The purpose of the game is for the player to guess what the secret number that the Streamlit game generated within a limited number of attempts. The player can select Difficulty, and the goal is to guess correctly using higher/lower hints while tracking score, attempts and guess history. 

Bug detail
- The first bug was in the guess-evaluation logic inside logic_utils.py (originally in app.py).
check_guess() was returning the wrong hint text for the comparison result.
- For example, when the user guessed too low, the app could still show “Go LOWER!” instead of “Go HIGHER!”, and vice versa.

Fixes applied
- Updated check_guess() so:
   - guess > secret returns "Too High" and "📉 Go LOWER!"
   - guess < secret returns "Too Low" and "📈 Go HIGHER!"
- Made sure the secret number is always turned into a normal integer before checking the guess, so the hint text stays correct every time.
- Added/verified tests in test_game_logic.py to assert the correct hint messages for both too-high and too-low guesses.

 
## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Player will input first guess (e.g., 50)
2. Player will then press enter or submit their guess by clicking on button.
3. Game will show a hint (e.g., "📈 Go HIGHER!" or "📉 Go LOWER!").
4. Attempts will be incremented.
5. Score will be updated.
6. If player does not guess the secret number, player will make another guess.
7. Continue until player guesses the correct number.
8. Game shows success(balloons), and displays the final score and set status to won. 
9. Player can click New Game to start a fresh game.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests\test_game_logicpy .....                                                                   [100%]

===================================== 5 passed in 1.05s ====================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
