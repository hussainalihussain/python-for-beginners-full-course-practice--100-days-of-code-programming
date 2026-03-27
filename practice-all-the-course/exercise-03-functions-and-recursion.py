"""
Exercise 03: Functions And Recursion

Focus:
- user-defined functions
- default arguments
- keyword arguments
- *args
- **kwargs
- docstrings
- recursion
"""


# Exercise 1:
# Write a function called average that takes any number of numeric values with *args
# and returns the average.
def exercise_1_average(*numbers):
    sum = 0
    size = len(numbers)
    size = 1 if size == 0 else size
    
    for number in numbers:
        sum += number
    
    return sum / size


# Exercise 2:
# Write a function called power(num, power=2) that behaves like your earlier lesson:
# if power is not given, square the number.
def exercise_2_power(num, power=2):
    return num ** power


# Exercise 3:
# Write a function called student_report(name, *marks, **details).
# It should print:
# - the student's name
# - average marks
# - any extra details passed in keyword form
def exercise_3_student_report(name, *marks, **details):
    print(f"Student name: {name}")

    total = 0

    for mark in marks:
        total += mark
    
    print(f"Average marks: {total / len(marks)}")
    
    for key in details:
        print(f"{key}: {details[key]}")


# Exercise 4:
# Add a proper docstring to a function called currency_converter(amount, rate).
# Return the converted amount and print the docstring using __doc__.

def exercise_4_currency_converter(amount, rate):
    """
    This is docstring of the exercise_4_currency_converter
    """
    print(exercise_4_currency_converter.__doc__)

    return amount * rate


# Exercise 5:
# Write a recursive factorial function.
# Example:
# factorial(5) -> 120
def exercise_5_factorial(number):
    if number == 0 or number == 1:
        return 1
    
    return number * exercise_5_factorial(number - 1)


# Exercise 6:
# Write a recursive Fibonacci function for the nth value.
# Then think about why this version gets slow for large numbers.
def exercise_6_fibonacci(number):
    '''
    Formula
        Base cases:
            F(0) = 0
            F(1) = 1
        
        F(N) = F(N-1) + F(N-2)
    '''
    
    if number == 0:
        return 0
    
    if number == 1:
        return 1
    
    return exercise_6_fibonacci(number - 1) + exercise_6_fibonacci(number - 2)


if __name__ == "__main__":
    # Exercise 1:
    # print(exercise_1_average(20, 25, 30, 35, 40))


    # Exercise 2:
    # num = 5
    # print(exercise_2_power(num))
    # print(exercise_2_power(num, 5))


    # Exercise 3:
    # exercise_3_student_report("Hussain Ali", 89, 59, 68, 93, status="Employee", profession="Full stack web developer")


    # Exercise 4:
    # exercise_4_currency_converter(500, 282)


    # Exercise 5:
    # number = 5
    # print(exercise_5_factorial(number))


    # Exercise 6:
    number = 5
    # F(5) = F(4) + F(3)
    #  = (F(3) + F(2)) + (F(2) + F(1))
    #  = ((F(2) + F(1)) + F(2)) + (F(2) + 1)                            : F(1) = 1
    #  = (((F(1) + F(0)) + 1) + (F(1) + F(0))) + ((F(1) + F(0)) + 1)
    #  = (((1 + 0) + 1) + (1 + 0)) + (1 + 0) + 1)                       : F(0) = 0, F(1) = 1
    #  = (2) + (1) + 2 = 5
    print(exercise_6_fibonacci(number))

