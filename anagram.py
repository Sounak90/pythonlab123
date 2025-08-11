from collections import Counter

str1 = input("Enter first word: ")
str2 = input("Enter second word: ")

if len(str1) == len(str2) and Counter(str1) == Counter(str2):
    print("It is a Anagram.")
else:
    print("It is not a Anagram.")