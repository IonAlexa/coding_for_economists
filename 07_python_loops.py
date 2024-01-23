#Let's have a look at loop synthax

#for loop operate on "iterables"

#Let's create an iterable object
myList = [1, 2, 'abc']

#Let's iterate over the object
for item in myList:
  #Loop body needs to be indented one
  print(item)

for item in myList:
  if item ==1:
    print(item)
  else:
    print("item not equal to 1.")

#Looping over a range of values
for i in range(5): #range () generates value on the fly
  print(i)

#Another way to do it

range_vals = [1, 2, 3, 4,] # not memory efficient
print("Using a list to display values 0-4" )
for i in range_vals:
    print(i)

#Looping over list of strings and nesting loops
for name in ['Alice', 'Bob', 'Charlie']:
  print(name)
  #Iterate through each strings
  for letter in name:
    print(letter)

#Using the enumerate() function to get both index and value
print("Using enumerate()")
for index, name in enumerate(['Alice', 'Bob', 'Charlie']):
  print(index,name)

#Equivalent loop using indexing
print("Using range() and indexing")
myList = ['Alice', 'Bob', 'Charlie']
for index in range(len(myList)): #range(3)
  print(index, myList[index])

#Use a loop to create a list of capital letters from A-Z
print("Using a loop to create a list of capital letters from A-Z")

#Intatiate an empty list to append to
alphabet = [chr(65)]

for i in range(66,91):
  alphabet.append(chr(i))

print(alphabet)

#while loops
#while loops are used when you don't know how many times you want to loop

#Instantiate counter variable
i = 0
while i < 10:
  #Will print something as long as i is smaller then 10
  print(i)
  #Increment our counter every iteration, otherwise it will loop forever
  i += 1

#List comprehensions

#Let's have a look at a for loop creating a list of squares from 0 to 10

squares = []
for num in range(0,11):
  squares.append(num**2)

print(squares)


# Doing the same using list comprehension

squares = [num**2 for num in range(0,11)]

print(squares)

#Using if statements in list comprehension

even_squares = [num**2 for num in range(0,11) if num % 2 == 0]

print(even_squares)
        


