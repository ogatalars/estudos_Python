with open("teste.txt") as file:
    print(file.read())


print(file.closed)


try:
    with open("test2.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("O arquivo não foi encontrado")
