a = 5
b = 5
c = a + b
print(c)

a = 10 - 5 / 2
b = 100 - 5 ** 3
result = a + b
print(result)

x = 99
y = 100 - x / 4 * (2 - x)
result = x + y
print(result)


numbers = [1, 2, 3, 4, 5]
print("Sum of numbers:", sum(numbers))


def add(x, y):
    return x + y


print("Result:", add(5, 10))

try:
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    print("Sum:", x + y)
except ValueError:
    print("Invalid input. Please enter numeric values.")
