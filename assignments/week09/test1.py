try:
    # input 3 ตัว
    number1 = float(input("ตัวเลขที่1: "))
    number2 = float(input("ตัวเลขที่2: "))
    operator = input("เครื่องหมาย (+,-,*,/): ")

    result = 0

    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2

    print(f"{number1} {operator} {number2} = {result}")

except ValueError:
    print("ต้องเป็นตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

finally:
    print("จบการทำงาน")