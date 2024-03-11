# 01_strings_exercise.ipynb

# 1. Fill missing pieces
# Fill ____ pieces below to have correct values for lower_cased, stripped and stripped_lower_case variables.

original = " Python strings are COOL! "
lower_cased = original.lower()
stripped = original.strip()
stripped_lower_cased = original.strip().lower()

assert lower_cased == " python strings are cool! "
assert stripped == "Python strings are COOL!"
assert stripped_lower_cased == "python strings are cool!"

# 2. Prettify ugly string
# Use str methods to convert ugly to wanted pretty.

ugly = " tiTle of MY new Book\n\n"
# Your implementation:
pretty = [i.capitalize() for i in ugly.split()]
pretty = ' '.join(pretty)

# Let's make sure that it does what we want. assert raises AssertionError if the statement is not True.
print(f"pretty: {pretty}")
assert pretty == "Title Of My New Book"

# 3. Format string based on existing variables
# Create sentence by using verb, language, and punctuation and any other strings you may need.

verb = "is"
language = "Python"
punctuation = "!"

# Your implementation:
sentence = ["Learning", language, verb, "fun"]
sentence = ' '.join(sentence) + punctuation

print(f"sentence: {sentence}")
assert sentence == "Learning Python is fun!"
