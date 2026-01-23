'''
01. union
02. intersection
03. difference
04. symmetric difference
05. disjoint
06. superset
07. subset
08. add an element to the set
09. update
10. remove vs
11. discard
12. pop (a random element pop)
13. del (keyword) - remove variable - similar to unset of php
14. clear (remove everything from the set)
15. "String" in set: Boolean

plus its update
'''


'''
1. Union
2. Union with update
'''
asian = {"Pakistan", "India", "China", "Afghanistan"}
european = {"Germany", "France", "Italy"}

# print(asian.union(european))
# print(asian, european)
# asian.update(european)
# print(asian)


'''
3. Intersection
4. Intersection with update
'''
names1 = {"Ali", "Wali", "Ahmad"}
names2 = {"Said", "Ahmad", "Jamal"}

# print(names1.intersection(names2))
# print(names1, names2)
# print(names1.intersection_update(names2))
# print(names1, names2)


'''
5. Symmetric Difference
'''
s1 = {1, 2, 3, 2, 5}
s2 = {2, 5, 6, 7}

# print(s1.symmetric_difference(s2))


'''
6. Disjoint
'''
s1 = {1, 2, 3, 2, 5}
s2 = {2, 5, 6, 7}
# print(s1.isdisjoint(s2))
s3 = {6, 7, 8, 9}
# print(s1.isdisjoint(s3))


'''
7. Superset
'''
s1 = {1, 2, 3, 4, 5, 6}
s2 = {3, 5}
s3 = {3, 5, 7}
# print(s1.issuperset(s2))
# print(s1.issuperset(s3))


'''
8. Subset
'''
# print(s2.issubset(s1))
# print(s3.issubset(s1))


'''
9. Add an element to the set
'''
info = {"Hussain", "Buner", "KPK"}
newItem = 5.8
# print(info)
info.add(newItem)
# print(info)



'''
10. Remove an element from the set - but if not found then raise error
11. Remove an element from the set - but don't raise error even if an element didn't exists
'''
info = {"Hussain", "Buner", "KPK"}
toRemoveItem = "Hussain"
toRemoveItem2 = "hussain"
# info.remove(toRemoveItem2) #
info.discard(toRemoveItem2)
# info.discard(toRemoveItem)
# print(info)


'''
12. del keyword
'''
info = {"Hussain", "Buner", "KPK"}

del info
# print(info)


'''
13. clear a set
'''
info = {"Hussain", "Buner", "KPK"}

# print(info)
# info.clear()
# print(info)


'''
14. pop an element - random element
'''
info = {"Hussain", "Buner", "KPK"}
removedItem = info.pop()
print(info)
print(removedItem)


'''
15. Find if an element exists in a set
'''
info = {"Hussain", "Buner", "KPK"}
searchFor = "KPK"
# print(searchFor in info)


'''
16. type of empty set
'''
set1 = {}
set2 = set()
print(type(set1))
print(type(set2))