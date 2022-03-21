# str.format()  = option method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The " + animal + "jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))
print("The {} jumped over the {}".format("Elephant", item))
print("The {1} jumped over the {0}".format(animal, item))
# print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon"))

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Ogata"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice too meet you".format(name))
print("Hello, my name is {:^10}. Nice too meet you".format(name))


number = 3.14159
print("The Number Pi is {}".format(number))
print("The Number Pi is {:.2f}".format(number))  # 2 decimal places
print("The Number Pi is {:.3f}".format(number))  # 3 decimal places

number1 = 10000
print("The number1 is {:.2e}".format(number1))
print("The number1 is {:b}".format(number1))
print("The number is {:x}".format(number1))  # hexadecimal
