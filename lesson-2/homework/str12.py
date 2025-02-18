words = str(input("Enter words separated by space: ")).split()
separator = input("Enter a separator character: ")
joined_string = separator.join(words)
print("Joined string:", joined_string)