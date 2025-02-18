name = str(input("Enter a string: "))
substring = str(input("Enter a substring to check: "))
if substring in name:
    print(f"'{substring}' is found in the string.")
else:
    print(f"'{substring}' is not found in the string.")