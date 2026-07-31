# รับค่า ชื่อจริง ผู้ใช้
# เขียน loop เพื่อนับจำนวน "สระที่อยู่ในชื่อที่รับมา" นั้นว่ามีจำนวนกี่ตัว

# ตัวอย่างหน้าจอ

# what is your name?  Boonchu
# Your name have 4 vowels.

name = "Boonchoo"
vowels = 0

for letter in name:
    print(f"ตัวอักษร : {letter}")

    if letter == 'a' or letter == 'A':
        vowels += 1
    elif letter == 'e' or letter == 'E':
        vowels += 1
    elif letter == 'i' or letter == 'I':
        vowels += 1
    elif letter == 'o' or letter == 'O':
        vowels += 1
    elif letter == 'u' or letter == 'U':
        vowels += 1

print("Your name has", vowels, "vowels")