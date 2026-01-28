# 🎓 3. Student Marks Analysis
# Scenario:
# * Convert marks to percentage
# * Select passed students (≥ 40%)
# * Calculate class average
#
# 📌 Use case: School result systems
# ⚠️ Note: filter() iterator is consumed — usually convert to list first


from functools import reduce

getPercantage = lambda marks: (marks * 100) / 100
sum = lambda x, y: x+y

marks = [78, 35, 90, 66, 42]
marks_in_percentage = list(map(getPercantage, marks))
passed_students = list(filter(lambda marks: marks >= 40, marks_in_percentage))
class_average = reduce(sum, marks) / 5

print('marks: ', marks)
print('marks in percentage: ', marks_in_percentage)
print('passed students: ', passed_students)
print('class average marks: ', class_average)



























# From chatgpt




# from functools import reduce

# marks = [78, 35, 90, 66, 42]

# percentages = map(lambda m: (m / 100) * 100, marks)
# passed = filter(lambda p: p >= 40, percentages)
# average = reduce(lambda a, b: a + b, passed) / len(list(passed))
