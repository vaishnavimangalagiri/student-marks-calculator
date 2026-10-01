name = input("Enter your name: ")
english = int(input("Enter your english marks: "))
maths = int(input("Enter your maths marks: "))
python = int(input("Enter your python marks: "))
print("Student name:", name)
print("English marks:", english)
print("Maths marks:", maths)
print("Python marks:", python)
total = english + maths + python
print("Total marks:", total)
percentage = (total / 300) * 100
print("percentage:", percentage)
if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Fail")
