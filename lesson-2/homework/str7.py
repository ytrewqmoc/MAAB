sentence = str(input("Enter a sentence: "))
replace_word = str(input("Enter the word to replace: "))
with_word = str(input("Enter the word to replace with: "))

replaced_sentence = sentence.replace(replace_word, with_word)
print("Updated sentence:", replaced_sentence)