sentence_for_acronym = str(input("Enter a sentence to create an acronym: "))
acronym = ''.join(word[0].upper() for word in sentence_for_acronym.split())
print("Acronym:", acronym)