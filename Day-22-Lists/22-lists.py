list = [92, 97, 90, 54, 19, 84]

for l in list:
  print(l)

print()

print(list[1])
print(list[3])


'''
Everything related to slicing in String and lists are same
so we will not do those things as already done, but we will give just example how we can use it:
list[:]
list[0:len(list)]
list[0:]
list[:len(list)]
list[-1:]
list[:-2]
list[-3:-1]
list[len(list)-3:len(list)-1]
list[1:3,2]
'''


'''
List comprehension
'''

lst = [i for i in range(6)]

print(lst)

lst = [i*2 for i in range(8)]
print(lst)

lst = [i for i in range(10) if i%2 == 0]
print(lst)

lst = [i for i in range(11) if i%2 == 0]
print(lst)



# Examples:
# 1. get the odd numbers upto 15
# 2. get the odd numbers upto 14
# 3. get the number divisible by 5 upto 40

odd = [i for i in range(1, 16) if i % 2 != 0]
print('odd:', odd)

even = [i for i in range(15) if i % 2 ==0]
print('even:', even)

divisibleBy5 = [i for i in range(1, 41) if i % 5 == 0]
print('divisible by 5:', divisibleBy5)