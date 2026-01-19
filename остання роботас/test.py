from main import seconds_to_minutes

def test_less_than_minute():
    assert seconds_to_minutes(45) == "00:45"

def test_exactly_one_minute():
    assert seconds_to_minutes(60) == "01:00"

def test_more_than_minute():
    assert seconds_to_minutes(125) == "02:05"
