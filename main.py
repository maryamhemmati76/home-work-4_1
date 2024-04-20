x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

from src.summation import add
from src.subtract import sub
from src.multiply import multiply

sum_ = add(x, y)
sub_ = sub(x, y)
multiply_ = multiply(x, y)

print(f"{x} + {y} = {sum_}")
print(f"{x} - {y} = {sub_}")
print(f"{x} * {y} = {multiply_}")


with open("calculaton.txt", "w") as file:
    file.write(f"summation is {sum_}")
    file.write(f"subtract is {sub_}")
    file.write(f"subtract is {multiply_}")