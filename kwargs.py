# **kwargs = parameter that will pack all arguments into a dictionary. Useful so that a function can accept multiple arguments.

# def hello(first, last):
#     print("Hello " + first + " " + last)


# hello(first="bro", last="dude")


def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
