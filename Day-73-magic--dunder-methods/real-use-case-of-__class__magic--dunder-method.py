import time
from RunningAverage import RunningAverage
from Timer import Timer
from Fibonacci import Fibonacci


# Example 1
avg = RunningAverage()

print(avg(10)) # 10 -> 10/1
print(avg(20)) # 15 -> 10+20 = 30, and count = 2 => 30/2 = 15
print(avg(30)) # 20 -> 10+20+30 = 60, and count = 3 => 60/3 = 20



# Example 2
'''
@Timer
def slow_function():
  ...

It is exactly the same as writing:
def slow_function():
    time.sleep(1)

slow_function = Timer(slow_function)



🧠 Step-by-Step Execution

Step 1 — Function is created
Python first creates:
def slow_function():
  time.sleep(1)

At this point, slow_function is a normal function.


Step 2 — Decorator runs
@Timer means:
slow_function = Timer(slow_function)

So now:
* Timer.__init__() runs
* The original function is stored in self.func
* slow_function is now a Timer object, not a function


Step 3 — You call it
When you run:
slow_function()

You're actually calling a Timer instance.
Python sees parentheses on an object and calls:
Timer.__call__()

So this runs:
def __call__(self, *args, **kwargs):


The execution flow becomes:
You call slow_function()
→ Timer.__call__()
→ original slow_function()
→ print execution time
→ return result
'''
print()
print("Timer")

@Timer
def show_function():
  time.sleep(1)

show_function()



# Example 3
print()
print("Fibonacci")
fib = Fibonacci()
print(fib(10))