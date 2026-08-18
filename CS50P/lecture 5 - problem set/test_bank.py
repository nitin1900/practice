from bank import value

def test_lowercase_bank():
    assert value("hello")==0
    assert value("hey, teacher")==20
    assert value("what's up bro?")==100


def test_uppercase_bank():
    assert value("HELLO HARVARD STUDENT")==0
    assert value("HOPE EVERYTHING IS GOOD")==20
    assert value("WHAT'S GOING ON?")==100


def test_capitalize_bank():
    assert value("Greeting Hello Miss")==100
    assert value("Honrable Mr. Fool")==20
    assert value("Hello Lady")==0

def test_user_mistake_bank():
    assert value("       HEllo")==0
    assert value("Hey      miSw")==20
    assert value("what's up poet")==100