# 1️⃣ Stateful Function (Cleaner than a Closure)
#  When you want a function that remembers state between calls, __call__ makes it clean and readable.
#  ✔ Useful when:
#    You need state
#    You want function-like syntax
#    You don’t want global variables


'''
This function will calculate the average on the fly
for example we have exam,
for the first day we add how much number he got,
second day he give the 2nd day marks (he don't need to add the first day marks again) and will get the average of two days
third day he give the 3rd day's marks (again he don't need to add the 1st and 2nd date to get average) and he will get the average of the 1-3rd day marks result average
and so on
'''
class RunningAverage:
  def __init__(self):
    self.total = 0
    self.count = 0
  
  def __call__(self, value):
    self.total += value
    self.count += 1

    return self.total / self.count
