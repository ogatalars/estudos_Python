# exception = events detected during execution that interrupt the flow of a program
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("something went wrong")
else:  # if no exception is raised
    print("Result is", result)
finally:
    print("This will always be printed")
