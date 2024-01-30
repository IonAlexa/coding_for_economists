#Task 1: Find the index position of the colum "WIN_COUNTRY_CODE"
#Hint: Grab the headers and assign them to a variable. Then, iterate through headers using enumerate()
f = open("data/raw/european_commission/ted-sample.csv")

headers = f.readline().strip().split(",")

f.close()


for index, value in enumerate(headers):
  print(index, value)

# Task 2: Instantiate an empty list called data

  data = []

#Task 3: Use the context manager open() and
# 3.1 Iterate through teach line of the csv file using the contect manager open()
#3.2 append the observation as a list. Hint: Use the .split() method on the line to authomatically create list

  with open("data/raw/european_commission/ted-sample.csv"") as f:
            for line in f:
    data.append(list(line.split(",")))


print(data[0]) 

# Output should look like: data[[row0], [row1], ..., [rowN]]]
data = data[1:]
#4. Count the number of wins by country

d = {}
for row in data:
  if not row [62] in data:
    country = row [61]
    countries = country.split('--- ') # Returns a list of winning countries
    for winning_country in countries:
    if not winning_country in d:
      d[winning_country] = 0
      d[winning_country] += 1


print(d)


  