name = str(input("Enter the string: "))
start_word = input("Enter the word the string should start with: ")
end_word = input("Enter the word the string should end with: ")

if name.startswith(start_word) and name.endswith(end_word):
    print("The string starts with", start_word, "and ends with", end_word)
else:
    print("The string does not start with", start_word, "or end with", end_word)