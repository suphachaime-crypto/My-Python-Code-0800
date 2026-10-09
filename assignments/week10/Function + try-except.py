def deposit(money):
    balance = 1000
    print(f"ยอดเงินเริ่มต้น: {balance} บาท")
 
    try:
        money = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
 
        if money <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
 
    except ValueError as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")
 
    else:
        balance += money
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
 
    finally:
        print("สิ้นสุดรายการฝากเงิน")
 
 
deposit(0)