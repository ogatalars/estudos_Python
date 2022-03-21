
import time

listaCompras = ["pizza", "pasta", "burger",
                "manteiga", "leite", "ovos", "queijo"]
listaCompras2 = ["Cerveja", "Carne", "Pão",
                 "arroz", "feijão", "farinha", "ovo", "queijo"]

# array JS = lista Python

# dadosPessoa = {
#     nome: "Keppe",
#     age: 31,
#     heigth: 1.78,
# }


# tuplas - Array/list só que com valores fixos.
ingredientes_bolo = ("manteiga", "farinha", "ovos", "leite", "queijo")


# dicionarios - OBJETO NO JS
ingredientesBolo = {
    "manteiga": "1 colher de sopa",
    "Farinha": "1 colher de sopa",
}
ingredientesBolo.update({"ovos": "2 unidades"})
print(ingredientesBolo)

# sets
ingredienteBolo2 = {"manteiga", "farinha", "ovos", "leite", "queijo", "queijo"}


# If and else
# if(a = 0) {
#     console.log("a é igual a 0")
# } else {
#     console.log("a não é igual a 0")
# }

a = 3
if (a == 0):
    print("a é igual a 0")
elif (a == 1):
    print("a é igual a 1")
elif(a >= 100):
    print("Esse número é muito grande")
else:
    print("a não é igual a 0")

# functions
# function soma(num1, num2) {return num1 + num2}
# soma = (num1, num2) = > {return num1 + num2}


def soma(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiplicacao(*args):
    total = 1
    for x in args:
        total *= x
    return total


# while e o for
# for x in range(0, 11):
#     print(x)

for seconds in range(10, 0, -2):
    print(seconds)
    time.sleep(2)
print("BOOOM!")


# JavaScript
# for(let i = 0; i < 10; i++) {
#     console.log(i)
# }
