name = input("What is your name?: ")
vowels = 0

for letter in name:
    print(f"ตัวอักษร: {letter}")
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowels = vowels + 1

print(f"Your name has {vowels} vowels.")