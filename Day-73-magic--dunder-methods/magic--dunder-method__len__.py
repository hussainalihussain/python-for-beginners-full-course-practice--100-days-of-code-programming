class Employee:
  name = "Hussain"

e = Employee()

# print(len(e)) # Error: has no len()


class Employee2:
  name = "Hussain"

  def __len__(self):
    return len(self.name)

e = Employee2()
print(len(e))