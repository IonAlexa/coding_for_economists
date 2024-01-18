#in this file we eill look at lists, dictionaries, sets, tiples, range

#List
myList =[1, 2, 3, 4, 5]

print(myList)

print(type(myList))

#Grab first object of list
print(myList[0])

#How many objects are in our list
print(len(myList))

#Nice thing about lists: they are flexible with respect to the data type

mixedList = [1, "two", 3.0, [4, "four"], 5]
print(mixedList)

#Add or remove objects from list
mixedList.append(6)

print(mixedList)

#Removing
mixedList.pop() #removes last item

#How many times does the integer 1 appear
print(mixedList.count(1))

#Reverse a list#
mixedList.reverse()
print(mixedList.reverse())