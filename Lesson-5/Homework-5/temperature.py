def convert_cel_to_far(c):
    return c*9/5 + 32

def convert_far_to_cel(f):
    return (f - 32)*5/9


c = float(input("Enter a temperature in degrees C: "))
farenheit = convert_cel_to_far(c)
print(f"{c} degrees C = {farenheit:.2f} degrees F")

print()

f = float(input("Enter a temperature in degrees F: "))
celcius = convert_far_to_cel(f)
print(f"{f} degrees F = {celcius:.2f} degrees C")
