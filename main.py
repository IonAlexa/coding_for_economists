#Exercise: Indexing and sclicing

url = 'https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv'


#Use indexing, slicing to fill in the following output
#Copy/past is not allowed

file_name = file_name = url[-14:]
print(filne_name) // 'ted-sample.csv'


protocol=protocol = url[0:5]
print(protocol) #'https'

host_name = host_name = url[8:18]
print(host_name #'github.com')

      #Use string composition to construct http://github.com/ted-sample.csv: output = protocol + '://' + host_name + "/" + file_name
      >>> print (output)
      