# Treino para fazer uma simples calculadora em Python
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def minus(*args):
    minus = 0
    for i in args:
        minus -= i
    return minus


def multiply(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply


def divide(*args):
    divide = 1
    for i in args:
        divide /= i
    return divide


def calculadora():
    numero1 = int(float(input("Digite o primeiro número: ")))
    numero2 = int(float(input("Digite o segundo número: ")))
    o_que_fazer = str(input(
        "Digite o número para a operação: 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão: "))
    if o_que_fazer == "1":
        print(add(numero1, numero2))
    elif o_que_fazer == "2":
        print(minus(numero1, numero2))
    elif o_que_fazer == "3":
        print(multiply(numero1, numero2))
    else:
        print(divide(numero1, numero2))


print(add(3, 4))
print(minus(5, 2))
print(multiply(2, 3))
print(divide(4, 2))
calculadora()
