text = input("Enter a text: ")
word = input("Enter a word: ")
if word.lower() in text.lower():
    print("Yes")
else:
    print("No")

