name = "Nandini"
name_length = len(name)
n = int(input("enter no.of students:"))
marks = [0] * n
for i in range(n):
    marks[i] = int(input("enter the marks of the student:"))
valid_count = 0
fail_count = 0
for mark in marks:
    if mark < 0 or mark > 100:
        category = "Invalid"
    else:
        valid_count = valid_count+1
        if mark >= 90:
            category = "Excellent"
        elif mark >= 75:
            category = "Very Good"
        elif mark >= 60:
            if name_length % 2 == 0 and mark == 60:
                category = "Very Good"
            else:
                category = "Good"
        elif mark >= 40:
            category = "Average"
        else:
            category = "Fail"
            fail_count = fail_count+1
    print(mark, "→", category)
print("Total Valid Students:", valid_count)
print("Total Failed Students:", fail_count)

