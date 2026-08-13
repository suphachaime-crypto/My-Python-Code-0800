scores = []
 
for i in range(5):
    score = int(input("Enter score of student " + str(i+1) + ": "))
    scores.append(score)
 
for i in range(5):
    if scores[i] >= 50:
        print("Student", i+1, ":", scores[i], "-> ผ่าน")
    else:
        print("Student", i+1, ":", scores[i], "-> ไม่ผ่าน")