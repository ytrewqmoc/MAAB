name = str(input("Enter a string: "))
vowels = "aeiouAEIOU"
symbol = input("Enter a symbol to replace vowels with: ")
string_with_symbols = ''.join(symbol if char in vowels else char for char in name)
print("String with vowels replaced:", string_with_symbols)