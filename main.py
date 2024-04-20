x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

from src.summation import add
sum_ = add(x, y)
print(f"{x} + {y} = {sum_}")

with open("calculaton.txt", "w") as file:
    file.write(f"summation is {sum_}")