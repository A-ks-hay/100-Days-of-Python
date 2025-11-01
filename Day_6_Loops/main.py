# for loop with range
for i in range(5):
    print(i)

# while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass statement
for i in range(3):
    pass  # used as a placeholder

# nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# using else with loop
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop completed successfully!")
