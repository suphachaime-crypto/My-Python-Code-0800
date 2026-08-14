def calculate_triangle_area(height, base):
    area = 0.5 * height * base
    print(f"Triangle with height {height} and base {base}")
    print(f"Area = 0.5 x {height} x {base} = {area}")
    print()
 
def calculate_rectangle_area(length, width):
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} x {width} = {area}")
    print()
 
def calculate_circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    print(f"Circle with radius {radius}")
    print(f"Area = {pi} x {radius}^2 = {area}")
    print()
 
print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)
 
print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)
 
print("Calculating circle areas:")
calculate_circle_area(4)
calculate_circle_area(7)

#เขียน function ชื่อ calculate_sphere(radius)
#คำนวนหา ปริมาณของทรงกลม
#volume = 4.0 / 3 * pi radius **
#จากนั้นเเสดงผลลัพธิ์ที่เหมาะสมออกจากหน้าจอ
#ไม่ลืมที่จะเขียนโปรแกรมในส่วนของการทดลองการใช้งาน
# ฟังก์ชันหาปริมาตรทรงกลม
def calculate_sphere(radius):
    pi = 3.14
    volume = 4.0 / 3 * pi * radius ** 3
    print(f"Sphere with radius {radius}")
    print(f"Volume = 4/3 x {pi} x {radius}^3 = {volume}")
    print()
 
 
# เรียกใช้งาน
print("Calculating sphere volumes:")
calculate_sphere(4)
calculate_sphere(7)