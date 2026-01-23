# averageMarks = int(input("Enter average marks: "))
averageMarks = 70

print("Grade A - Eligible for the admission") if averageMarks >= 80 else print("No Grade A - Not eligible for the admission")

'''
🍼 Example 1 — Candy decision
'''

finishedWork = False
finishedWork = True

reward = "Candy" if finishedWork else "No Candy"

print(f"Your reward: {reward}")


'''
🧸 Example 2 — Cold or Hot weather
'''

isCold = True
# isCold = False

clothes = "Jacket" if isCold else "T-shirt"

print(f"You need to wear {clothes}")


'''
🚲 Example 3 — Can you ride the bicycle?
'''

age = 18
age = 9

bike = "Big bicycle" if age >= 10 else "Small bicycle"

print(f"According to your age ({age}) you can drive {bike}")


'''
🧸 Example 1 — Weather chooser

Child style:

If temperature > 30 → “Too Hot”

Else if temperature > 20 → “Warm”

Else → “Cold”
'''

temprature = 31
# temprature = 21
# temprature = 15


weather = "Too Hot" if temprature > 30 else "Warm" if temprature > 20 else "Cold"

print(f"The weather is {weather}")



'''
🍭 Example 2 — School grade

If marks ≥ 90 → A

Else if marks ≥ 80 → B

Else if marks ≥ 70 → C

Else → Fail
'''
averageMarks = 90
# averageMarks = 80
# averageMarks = 70
# averageMarks = 50

grade = "Grade A" if averageMarks >= 90 else "Grade B" if averageMarks >= 80 else "Grade C" if averageMarks >= 70 else "Fail"

print(f"Your grade in marks is {grade}")