sentence = input("Write a sentence: ")

firstletters = [word[0] for word in sentence.split()]
print(''.join(firstletters))
