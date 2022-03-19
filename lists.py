# list = lista são usadas para guardar multiplos dados itens com uma variavel única

food = ['pizza', 'pasta', 'burger']  # lista com 3 itens
print(food)
print(food[0])  # primeiro item da lista
print(food[1])  # segundo item da lista
print(food[2])
# print(food[3])  # não existe item 3

food.append("Ice-cream")
food.remove("pasta")
food.append("pasta-x")
food.pop()
food.insert(0, "cake")


for x in food:
    print(x)


print(food.sort())
food.clear()  # limpa a lista
