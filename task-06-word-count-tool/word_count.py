from collections import Counter
import string

file_path = "sample.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    if text.strip() == "":
        print("The file is empty!")
    else:
        print("File read successfully!")

        words = text.split()
        word_count = len(words)
        print(f"Total words: {word_count}")
    
        lines = text.splitlines()
        line_count = len(lines)
        print(f"Total lines: {line_count}")
    
        character_count = len(text)
        print(f"Total characters: {character_count}")
    
        text_lowercase = text.lower()
        cleaned_text = text_lowercase.translate(str.maketrans('', '', string.punctuation))
        cleaned_text = cleaned_text.split()
    
        frequency_counter = Counter(cleaned_text)
    
        print("\nWord Frequency Distribution")
        for word, count in frequency_counter.items():
            print(f"{word}: {count}")
    
        print("\nTop 5 Most Common Words")
        for word, count in frequency_counter.most_common(5):
            print(f"{word}: {count}")

except FileNotFoundError:
    print("The file was not found.")