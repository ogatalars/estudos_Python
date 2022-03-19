# if statements = if, elif, else. Um bloco de código que só é executado se a condição for verdadeira.

age = int(input("How old are you? "))

if age == 100:
    print('Você é tem cem anos!')
elif age >= 18:
    print("Você é um adulto")
elif age < 0:
    print("Você não nasceu ainda")
else:
    print("Você é menor de idade")
