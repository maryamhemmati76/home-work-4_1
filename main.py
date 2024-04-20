x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

from src.summation import add
from src.subtract import sub
from src.multiply import multiply
from src.divide import divide

sum_ = add(x, y)
sub_ = sub(x, y)
multiply_ = multiply(x, y)
div = divide(x, y)

print(f"{x} + {y} = {sum_}")
print(f"{x} - {y} = {sub_}")
print(f"{x} * {y} = {multiply_}")
print(f"{x} / {y} = {div}")


with open("calculaton.txt", "w") as file:
    file.write(f"summation is: {sum_}\n")
    file.write(f"subtract is: {sub_}\n")
    file.write(f"subtract is: {multiply_}\n")
    file.write(f"divide is: {div}")