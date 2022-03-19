# set = collection which is unorded, unidexed. No duplcates values
utensils = {"knife", "spoon", "fork", "spoon",
            "spoon", "spoon"}  # parece objeto em js

for x in utensils:
    print(x)

utensils.add("plate")
utensils.remove("spoon")
print(utensils)
utensils.clear  # remove tudo.

dishes = {"bowl", "plate", "cup"}

utensils.update(dishes)  # adiciona todos os itens de dishes na utensils
dishes.update(utensils)  # adiciona todos os itens de utensils na dishes

# une todos os itens de utensils e dishes
dinner_table = utensils.union(dishes)

print(dinner_table)

# mostra itens de utensils que não estão em dishes
print(utensils.difference(dishes))

# Mostra itens que são iguais em utensils e dishes
print(utensils.intersection(dishes))
