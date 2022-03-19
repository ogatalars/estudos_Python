# Dictionary: a changeable data structure, unorded collection of unique keys: value pairs. Fast because they use Hashing

capitals = {"Usa": "Washington DC",
            "Brazil": "Brasilia",
            "india": "New Delhi",
            "UK": "London",
            "Russia": "Moscow"}
# parece um pouco sets, mas tem a virgula para separar e é changeable.
print(capitals["Russia"])
# print(capitals["Germany"])

print(capitals.get('Germany'))  # retorna None pois não existe germany

print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({"Germany": "Berlin"})
capitals.update({"usa": "California"})
capitals.pop()  # remove o ultimo item
# capitals.clear() # remove todos os itens

for key, value in capitals.items():
    print(key, value)
