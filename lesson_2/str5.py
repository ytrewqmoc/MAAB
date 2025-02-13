name = str(input("Enter a string: "))
vowels = "aeiouAEIOU"
num_vowels = sum(1 for char in name if char in vowels)
num_consonants = sum(1 for char in name if char.isalpha() and char not in vowels)
print(f"Vowels: {num_vowels}, Consonants: {num_consonants}")