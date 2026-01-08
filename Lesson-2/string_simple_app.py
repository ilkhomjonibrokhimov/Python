'''
name = 'John' # input("What's your name? ")
age = 45 # int(input("What's your age? "))

print("Your name is", name, "and your age is", age)
print("Your name is " + name + " and your age is " + str(age))
print(f"Your name is {name} and your age is {age}")
print("Your name is {fname} and your age is {fage}".format(fname = name, fage = age))
print("Your name is {} and your age is {}".format(name, age))


n = 34.454958734
print(f'{n=}')
print(f'{n:.2f}')

name1 = "Adam"
name2 = "Johnatan"
print(f"{name1:<10} - first name")
print(f"{name2:<10} - second name")

'''

mystr = "Hello world"
print(len(mystr))

# slicing or Indexing

# print(mystr[:4] + mystr[6:])
#print(mystr[0:20:2])
#print(mystr[::2])
print(mystr[-5:])
