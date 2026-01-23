def sumMarks(marks):
  total = 0

  for singleMarks in marks:
    total += float(singleMarks)
  
  return total

file = open('students.txt')

while True:
  studentData = file.readline()

  if not studentData:
    break

  # print(studentData)

  splitted = studentData.split(':')
  marks = splitted[1].split(',')

  # print(splitted, marks)
  totalMarks = sumMarks(marks)
  print(f"{splitted[0]}")
  print(f"Marks: {totalMarks}" + '\n')


