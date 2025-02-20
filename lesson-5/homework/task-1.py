def convert_cel_to_far(celsius):
    return celsius * 9/5 + 32

def convert_far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit} degrees F is {celsius:.2f} degrees C")

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = convert_cel_to_far(celsius)
print(f"{celsius} degrees C is {fahrenheit:.2f} degrees F")