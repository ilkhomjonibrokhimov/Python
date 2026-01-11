from datetime import date
name = input("Write your name: ")
yearob = int(input("Write your year of birth: "))

age = date.today().year - yearob
print(f"Your name is {name} and your age is {age}")
