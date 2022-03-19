# tuples = collection which is ordered and unchangeable. used to group together related data

student = ("Bro", 31, "M", "IT")
print(student.count(31))
print(student.index("M"))

for x in student:
    print(x)
if "Bro" in student:
    print("Bro is in the tuple")

# Tuplas são parecidas com listas, mas não mudam.
