from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    # and message should say "Go LOWER!" (bug fix: was "Go HIGHER!")
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    # and message should say "Go HIGHER!" (bug fix: was "Go LOWER!")
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_string_secret_numeric_comparison():
    # Regression test for the bug where the secret was converted to a string
    # and compared lexicographically(as text) instead of numerically.
    outcome, message = check_guess(40, "100")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_new_game_runtime_resets_status(monkeypatch):
    # Regression test for: when New Game button is clicked, reset_game_state() should set status back to "playing"
    # This ensures the player can submit guesses after starting a new game
    import app
    from types import SimpleNamespace

    # Create a mock session state that simulates a lost game
    fake_state = SimpleNamespace(attempts=5, secret=42, status="lost")
    
    # Monkey-patch app.st.session_state to use our fake state instead of real Streamlit state
    monkeypatch.setattr(app.st, "session_state", fake_state)
    
    # Monkey-patch random.randint to return a predictable secret (99) instead of random
    monkeypatch.setattr(app.random, "randint", lambda low, high: 99)

    # Call the reset_game_state() function to simulate clicking "New Game"
    app.reset_game_state()

    # Verify that the state was properly reset:
    assert fake_state.attempts == 0  # attempts counter should reset to 0
    assert fake_state.secret == 99  # secret should be regenerated
    assert fake_state.status == "playing"  # status must be "playing" so new guesses are accepted
