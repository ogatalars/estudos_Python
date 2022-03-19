# Slicing = create a substring by extracting elements from another string or sequence
# Slice pode conter um começo, uma parada e um fim
name = "Bro Code"
first_letter = name[0]
first_name = name[0:3]
last_name = name[4:8]
funky_name = name[0:8:2]
reversed_name = name[::-1]

print(first_letter)
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)
print(website[slice])
print(website2[slice])
