attendance = float(input("Attendance (%): "))
homework = float(input("Homework average: "))

can_take_exam = attendance >= 75 and homework >= 60

if can_take_exam:
    print("Eligible for exam")
else:
    print("Not eligible for exam")