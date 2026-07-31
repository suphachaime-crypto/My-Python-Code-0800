# รับค่า ชื่อจริง ผู้ใช้
# เขียน loop เพื่อนับจำนวน "สระที่อยู่ในชื่อที่รับมา" นั้นว่ามีจำนวนกี่ตัว

# ตัวอย่างหน้าจอ

# what is your name?  Boonchu
# Your name have 4 vowels.

name = input("What is your name?: ")

vowels = 0

for letter in name:
    print(f"ตัวอักษร : {letter}")

    if letter == 'a' or letter == 'A':
        vowels = vowels + 1

    if letter == 'e' or letter == 'E':
        vowels = vowels + 1

print("Your name have", vowels, "vowels")