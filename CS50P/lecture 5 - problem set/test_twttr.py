#not like that like this done by ai(below code)


from twttr import shorten

def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_uppercase_vowels():
    assert shorten("APPLE") == "PPL"
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("Hello, World.") == "Hll, Wrld."

def test_numbers():
    assert shorten("12345") == "12345"