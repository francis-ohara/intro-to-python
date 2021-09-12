"""
script for printing out Number of Words and Number of Characters in imported text files.
"""
# Import example text files
fh_money = open("money.txt")
money = fh_money.read()
fh_sign = open("sign.txt")
sign = fh_sign.read()


# Counter Functions
def char_counter(text: str) -> int:
    """Returns number of characters in argument string"""
    return sum([len(word) for word in text.split()])


def word_counter(text: str) -> int:
    """Returns number of words in argument string"""
    return len(text.split())


# Tests
print(f"There are {word_counter(money)} words and {char_counter(money)} characters in money.txt")
print(f"There are {word_counter(sign)} words and {char_counter(sign)} characters in sign.txt")
