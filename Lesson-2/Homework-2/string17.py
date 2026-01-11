text = input("Write a text: ")

result = ''
vowels = 'aeiou'
for char in text:
    if char.lower() in vowels:
        result += '*'
    else:
        result += char

print(result)
