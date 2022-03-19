# Nested loops = the inner loop will finish all of its iterations before finishing the outer loop.
rows = int(input("How many rows? "))
collums = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")
for i in range(rows):
    for j in range(collums):
        print(symbol, end="")
    print()
