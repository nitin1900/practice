from plate import is_valid

def test_plate_is_valid():
    assert is_valid("HELLO")==True
    assert is_valid("HELLO, WORLD")==False
    assert is_valid("GOODBYE")==False
    assert is_valid("CS50")==True
    assert is_valid("CS05")== False
    assert is_valid("50")==False