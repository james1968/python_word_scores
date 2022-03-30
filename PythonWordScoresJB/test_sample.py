from highscoringwords import HighScoringWords

# basic test to ensure the returned list is the correct length and first record is correct
def test_score():
    x = HighScoringWords()
    assert len(x.build_leaderboard_for_word_list()) == 100
    assert x.build_leaderboard_for_word_list()[0] == {'word': 'razzamatazzes', 'score': 51}

# basic test for the leaderboard function
def test_leaderboard():
    x = HighScoringWords()
    assert x.build_leaderboard_for_letters()




test_score()
