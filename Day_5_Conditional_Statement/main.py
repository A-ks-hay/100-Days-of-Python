# Simple if
age = 20
if age >= 18:
    print("You are eligible to vote.")

# if-else
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if-elif-else ladder
marks = 85
if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# Nested if
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive and Even number")

# Ternary Operator
age = 18
result = "Adult" if age >= 18 else "Minor"
print(result)
