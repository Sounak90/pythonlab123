from collections import Counter
import string
a = input("Enter a string: ")
a = a.lower()
translator = str.maketrans('', '',string.punctuation)
text = a.translate(translator)
c = text.split()
b = Counter(c)
print(b)