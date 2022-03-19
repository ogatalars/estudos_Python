# logical operators são operadores lógicos que permitem fazer comparações entre variáveis. Normalmente and e or são usados.
temp = int(input("Qual é a temperatura lá fora?"))

if temp >= 0 and temp <= 30:
    print("Esta numa temperatura agradável hoje")
    print("Vamos sair")
# ambas devem ser verdadeiras
elif temp < 0 or temp > 30:
    print("Esta numa temperatura ruim hoje")
    print("Fique em casa")
# elif not (temp >= 0 and temp <= 30):
#     print("Temperatura inválida")
# # Operador not
