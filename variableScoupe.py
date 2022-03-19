# scope = the region of the program where a variable is visible and recognized

def display_name():
    name = "code"
    print(name)


# print(name)  # NameError: name 'name' is not defined

# Global variable tem um escopo geral, global que pega em todos os lugares

name = "code"
print(name)
