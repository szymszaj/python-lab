for i in range(5):
    print('this in number', i)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print('this is number', n)

for idx, val in enumerate(numbers):
    print(f"Index {idx}: value {val}")

for n in numbers:
    if n > 25:
        print(f"{n} is bigger than 25")
