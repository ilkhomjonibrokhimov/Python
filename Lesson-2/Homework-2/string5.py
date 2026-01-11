word = input("word: ")

count_vowel = 0
count_cons = 0
for char in word.lower():
    if char in "aeiou":
        count_vowel += 1
    else:
        count_cons += 1

print("Vowels: ", count_vowel)
print("Consenants: ", count_cons)


