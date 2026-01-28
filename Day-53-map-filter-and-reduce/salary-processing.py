# 🏦 1. Salary Processing (HR / Payroll)
# Scenario:
# You have employee salaries.
# * Increase all salaries by 10%
# * Keep only salaries above 50,000
# * Find total salary expense
#
# 📌 Use case: Budget planning, payroll analytics

from functools import reduce

def increaseSalary (salary):
  return salary + salary * 0.1

def isHigherSalary (salary):
  return salary > 50_000

salaries = [30000, 45000, 60000, 80000, 25000]

updatedSalaries = list(map(increaseSalary, salaries))

higherSalaries = list(filter(isHigherSalary, updatedSalaries))

total_expense = reduce(lambda x, y: x + y, higherSalaries, 0)

print('salaries', salaries)
print('new Salaries: ', updatedSalaries)
print('higher salareis: ', higherSalaries)
print('higher salaries expense: ', total_expense)

