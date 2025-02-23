import os
import string
from collections import Counter

def get_text():
    if not os.path.exists("sample.txt"):
        print("sample.txt not found. Please enter text to create the file:")
        text = input("Enter text: ")
        with open("sample.txt", "w") as file:
            file.write(text)

def count_words():
    with open("sample.txt", "r") as file:
        text = file.read().lower()
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_count = Counter(words)
    return word_count, len(words)

def save_report(word_count, total_words):
    top_words = word_count.most_common(5)
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

def main():
    get_text()
    word_count, total_words = count_words()
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in word_count.most_common(5):
        print(f"{word} - {count} times")
    save_report(word_count, total_words)
    print("Word count report saved to word_count_report.txt")

if __name__ == "__main__":
    main()