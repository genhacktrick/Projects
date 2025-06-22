import json
from zxcvbn import zxcvbn
import nltk
from itertools import permutations
import datetime

# Download required corpus
nltk.download('words')
from nltk.corpus import words

def analyze_password_strength(password):
    print("\n🔍 Password Analysis:")
    result = zxcvbn(password)
    print(f"Score (0-4): {result['score']}")
    print(f"Feedback: {result['feedback']['warning']}")
    print(f"Suggestions: {', '.join(result['feedback']['suggestions'])}")
    print(f"Guesses: {result['guesses']}")
    print(f"Crack Time: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")

def generate_custom_wordlist(name, pet, birth_year):
    print("\n🛠 Generating Wordlist...")
    base_words = [name.lower(), pet.lower(), str(birth_year)]

    # Add common patterns
    patterns = ['123', '!', '@', '#', '2024', '2025']
    wordlist = set()

    for word in base_words:
        wordlist.add(word)
        for pat in patterns:
            wordlist.add(word + pat)
            wordlist.add(pat + word)

    # Add permutations
    for perm in permutations(base_words, 2):
        wordlist.add(''.join(perm))
        wordlist.add(''.join(reversed(perm)))

    print(f"✅ Wordlist Generated: {len(wordlist)} entries")
    return wordlist

def save_wordlist(wordlist, filename='custom_wordlist.txt'):
    with open(filename, 'w') as f:
        for word in sorted(wordlist):
            f.write(word + '\n')
    print(f"📁 Saved to: {filename}")

def main():
    print("🔐 Password Strength Analyzer + Wordlist Generator 🔐")
    password = input("Enter a password to analyze: ")
    analyze_password_strength(password)

    name = input("\nEnter your name: ")
    pet = input("Enter your pet's name: ")
    birth_year = input("Enter your birth year: ")

    wordlist = generate_custom_wordlist(name, pet, birth_year)
    save_wordlist(wordlist)

if __name__ == '__main__':
    main()
