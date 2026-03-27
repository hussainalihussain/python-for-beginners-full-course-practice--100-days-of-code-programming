"""
Exercise 01: Fundamentals

Focus:
- print and comments
- variables
- simple arithmetic
- user input
- type casting
- beginner challenge logic
"""


# Exercise 1:
# Print a three-line "student card" with your name, current goal, and favorite topic.
# Use at least one f-string and at least one escape sequence.
def exercise_1_student_card():
    print(f"Name: Hussain Ali \nGoal: Millionaire \nFavorite Topic: Development")


# Exercise 2:
# Ask the user for two numbers and print:
# - sum
# - difference
# - product
# - division
# Convert input values to numbers before calculation.
def exercise_2_basic_calculator():
    n1 = float(input("Enter Number1: "))
    n2 = float(input("Enter Number2: "))

    print(f"sum: {n1+n2}")
    print(f"difference: {n1-n2}")
    print(f"product: {n1*n2}")

    print(f"division: {n1/n2}")


# Exercise 3:
# Recreate a small type-casting exercise:
# Ask for the price of three items as input strings.
# Convert them to integers or floats and print the total bill.
def exercise_3_total_bill():
    mouse = float(input("Price of mouse? "))
    keyboard = float(input("Price of keyboard? "))
    usb = float(input("Price of usb? "))

    print(f"Sum of the bill: {mouse+keyboard+usb}")

# Exercise 4:
# Based on your early challenge files:
# Write a function that counts how many times a target character appears in a text.
# Example idea:
# count_char("banana", "a") -> 3
def exercise_4_count_char(text, target):
    count = 0

    for txt in text:
        # valid solution, since txt is already one character so target == txt is the correct check
        # if (target == txt): 

        if (target in txt): # but i used 'in' operator
            count += 1
    
    return count    


# Exercise 5:
# Based on the product_digits challenge:
# Write a function that receives an integer and returns the product of its digits.
# Example:
# 234 -> 2 * 3 * 4 = 24
def exercise_5_product_digits(number):
    '''
    Basic Logic:
        # n = 234
        # reminder = 234 % 10 = 4

        # n = int(234 / 10) = 23
        # reminder = 23 % 10 = 3

        # n = int(23 / 10) = 2
        # reminder = 2 % 10 = 2
    '''
    if number < 10:
        return number
    
    reminder = number % 10
    divider = int(number / 10)

    return reminder * exercise_5_product_digits(divider)





if __name__ == "__main__":
    # Exercise# 1
    exercise_1_student_card()


    # Exercise# 2
    # exercise_2_basic_calculator()


    # Exercise# 3
    # exercise_3_total_bill()


    # Exercise# 4
    text = "banana"
    to_search = "a"
    count = exercise_4_count_char(text, to_search)
    print(f"Text: {text}, searching: {to_search} \nCharacters Found: {count}")



    # Exercise# 5
    # n = 234
    # n = 230
    # n = 515
    # n = 156
    # n = 256
    # print(f"Product of {n}: {exercise_5_product_digits(n)}")