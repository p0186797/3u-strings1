sentence = input()
sentence = sentence.lower()
vowels = sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u")
print(vowels)
