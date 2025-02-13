name = str(input("Enter a string: "))
char_to_remove = input("Enter the character to remove from the string: ")
string_without_char = name.replace(char_to_remove, "")
print("String without the character:", string_without_char)