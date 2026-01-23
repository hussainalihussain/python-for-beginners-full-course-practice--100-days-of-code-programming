str = "My name is {} and i am living in {}"
info = "My name is {0} and i am living in {1}"
info2 = "My name is {1} and i am living in {0}"
taxInfo = "Total tax you need to pay {tax:.2f}"
name = "Hussain"
country = "Pakistan"

print(str.format(name, country))
print(info.format(name, country))
print(info2.format(country, name))
print(taxInfo.format(tax=16.1934))


name="Hussain"
organization="ITO"
welcomeMessage = f"Welcome {name} to our {organization} organization!"
print(welcomeMessage)

tax = 1550.2413
taxMessage = f"You need to pay {tax:.2f}$ of tax!"
print(taxMessage)

print("Sum using f-string:")
print(f"{2+3}")
print(type(f"2+3"))


literalMessage = f"This is an example of {{1,2,3}} of a mathematics set!"
print(literalMessage)