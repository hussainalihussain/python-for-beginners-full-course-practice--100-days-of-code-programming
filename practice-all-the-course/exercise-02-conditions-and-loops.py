import math

"""
Exercise 02: Conditions And Loops

Focus:
- if, elif, else
- match-case
- for loop
- while loop
- break and continue
- shorthand if-else
- for-else
"""


# Exercise 1:
# Ask the user for marks and print grade categories:
# A, B, C, D, or Fail.
# Add one extra condition for invalid marks below 0 or above 100.
def exercise_1_grade_checker():
    total_subjects = int(input("Total subjects: "))
    total_marks = 0

    for i in range(total_subjects):
        while True:
            subject_marks = float(input(f"Marks of {i+1}: "))

            if subject_marks < 0 or subject_marks > 100:
                print("Invalid marks: below 0 or above 100.")
                continue
            
            total_marks += subject_marks
            break
    
    average = total_marks / total_subjects

    if average >= 80:
        print('A')

    elif average >= 70:
        print('B')
    
    elif average >= 60:
        print('C')

    elif average >= 50:
        print('D')
    else:
        print('Fail')
        
        
        



# Exercise 2:
# Build a mini calculator using match-case.
# Supported operators: +, -, *, /
# The user should enter two numbers and one operator.
def exercise_2_match_case_calculator():
    n1 = float(input("Enter number 1: "))
    n2 = float(input("Enter number 2: "))

    while True:
        op = input('Enter operator (+, -, *, /): ')

        if op == '+':
            return  n2 + n1
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        elif op == '/':
            return n1 / n2
        else:
            print(f"\n'{op}' is not allowed operator!\nAllowed operators are: +, -, *, /\n")
            continue

        break



# Exercise 3:
# Use a for loop to print the multiplication table of a user-provided number.
# Then print the sum of the table results.
def exercise_3_multiplication_table():
    n = int(input("Number to get multiplication of: "))

    for i in range(10):
        print(f"{(i+1)}*{n} = {(i+1)*n}")


# Exercise 4:
# Use a while loop to keep asking for a password until the correct password is entered.
# Use continue if the user enters an empty value.
# Use break once the password is correct.
def exercise_4_password_loop():
    password = input("Enter password: ")

    while True:
        confirm_password = input("Confirm password: ")
        
        if not confirm_password:
            continue

        if confirm_password == password:
            print("Password confirmed")
            break

        print("\nInvalid Password, plz try again\n")


# Exercise 5:
# Write a prime number checker using for-else.
# Print whether the given number is prime or not.
'''
Simple logic:

if number is less than 2, it is not prime
try every number from 2 up to number - 1
if any one divides evenly, it is not prime
if none divide evenly, it is prime
'''
def exercise_5_prime_checker(number):
    if number < 2:
        print(f"{number} is not prime")
        return
    
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime (i.e., {number}/{i}={number/i})")
            break
    else:
        print(f"{number} is prime")


# Exercise 6:
# Practice shorthand if-else:
# Given a number, print "Even" if it is divisible by 2, otherwise print "Odd".
# Write it in one line first, then rewrite it using normal if-else.
def exercise_6_even_or_odd(number):
    print("Even" if number % 2 == 0 else "Odd")
    
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    # Exercise 1:
    # exercise_1_grade_checker()
    
    
    # Exercise 2:
    # print(exercise_2_match_case_calculator())


    # Exercise 3:
    # exercise_3_multiplication_table()


    # Exercise 4:
    # exercise_4_password_loop()

    
    # Exercise 5:
    number = 51
    exercise_5_prime_checker(number)


    # Exercise 6:
    number = 21
    # exercise_6_even_or_odd(number)
