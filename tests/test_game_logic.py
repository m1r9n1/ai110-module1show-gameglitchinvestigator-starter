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
