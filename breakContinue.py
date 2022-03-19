# Loop control statements = Change a loops execution from its normal sequence

# break = used to terminate the loop entirely.
# continue = skips to  the next iteration of the loop.
# pass = does nothing, acts a placeholder

while True:
    name = str(input("Enter your name: "))
    if name != "":
        break


phone_number = "123-445-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
