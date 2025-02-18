name = str(input("Enter a string: "))
if any(char.isdigit() for char in name):
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")