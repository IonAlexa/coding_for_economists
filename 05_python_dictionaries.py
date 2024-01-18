#Intro to data type set

#set is a collection of well defined objects
mySet = {1,2,3,4,5,6,7,8,9,10}
print(mySet)


#Check type
print(type(mySet))

#Sets only contain uniquw values
mySet = {1,2,3,3,} #duplicate 3 gets removed
print(mySet)

#Define two sets and check out set operations
setA = {1,2,3}
listB = [3, 4, 5, ,5,5]
setB = set(listB)

print(setA, setB)

#set union
print(setA | setB)
unionAB = setA | setB
print(unionAB)

#intersection 
intersecAB = setA & setB
print(intersecAB)