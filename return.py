# Return statement = functions send Python values/objects back to the caller. These values/objects are called return values.
# Return statements are used to return a value from a function.

# def multiply(num1, num2):
#     result = num1 * num2
#     return result


def multiply(num1, num2):
    return num1 * num2


multiply(6, 8)  # Não vai imprimir
print(multiply(6, 8))
y = multiply(10, 20)
print(y)
