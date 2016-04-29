import re

_WORD_SPLIT = re.compile("([.,!?\"':;)(])")
_DIGIT_RE = re.compile(r"\d")

sentence = "The quick brown fox jumped\nover the lazy dogs."

words = []
for space_separated_fragment in sentence.strip().split():
    words.extend(re.split(_WORD_SPLIT, space_separated_fragment))

tokens = [w for w in words if w]

for x in tokens:
    print(x)
