text = input("Write a text: ")


if any(char.isdigit() for char in text):
    print("your text contains digits")
else:
    print("Your text doesn't contain any digit")

