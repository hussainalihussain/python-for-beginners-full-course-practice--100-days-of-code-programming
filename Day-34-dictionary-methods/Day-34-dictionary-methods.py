'''
1. update
'''
dict = {
  "affect": "To influence or cause a change in something or someone.",
  "decide": "To make a choice or judgment about something after thinking about it.",
  "develop": "To grow or cause to grow and become more advanced.",
  "knowledge": "Understanding of a subject that you get by experience or education.",
  "value": "The importance, worth, or usefulness of something.",
}
moreUsefulWords = {
  "Structure": "The way in which parts are arranged or organized to form a whole.",
  "Understand": "To know the meaning of something; to have a clear idea of how something works.",
}

# print(dict)
dict.update(moreUsefulWords)
# print(dict)


'''
2. clear
'''
dict.clear()
# print(dict)


'''
3. empty dictionary
'''
emptyDict = {}
# print(emptyDict)

'''
4. pop
'''
dict = {
  "affect": "To influence or cause a change in something or someone.",
  "decide": "To make a choice or judgment about something after thinking about it.",
  "develop": "To grow or cause to grow and become more advanced.",
  "knowledge": "Understanding of a subject that you get by experience or education.",
  "value": "The importance, worth, or usefulness of something.",
}

dict.pop("develop")
# print(dict)


'''
5. pop from end
'''
dict = {
  "affect": "To influence or cause a change in something or someone.",
  "decide": "To make a choice or judgment about something after thinking about it.",
  "develop": "To grow or cause to grow and become more advanced.",
  "knowledge": "Understanding of a subject that you get by experience or education.",
  "value": "The importance, worth, or usefulness of something.",
}
dict.popitem()

# print(dict)

'''
6. del
'''
dict2 = {
  "affect": "To influence or cause a change in something or someone.",
  "decide": "To make a choice or judgment about something after thinking about it.",
  "develop": "To grow or cause to grow and become more advanced.",
  "knowledge": "Understanding of a subject that you get by experience or education.",
  "value": "The importance, worth, or usefulness of something.",
}
del dict2
# print(dict2)


dict3 = {
  "affect": "To influence or cause a change in something or someone.",
  "decide": "To make a choice or judgment about something after thinking about it.",
  "develop": "To grow or cause to grow and become more advanced.",
  "knowledge": "Understanding of a subject that you get by experience or education.",
  "value": "The importance, worth, or usefulness of something.",
}

del dict3['affect']
print(dict3)