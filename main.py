x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

from src.summation import add
from src.subtract import sub

sum_ = add(x, y)
sub_ = sub(x, y)
print(f"{x} + {y} = {sum_}")
print(f"{x} - {y} = {sub_}")


with open("calculaton.txt", "w") as file:
    file.write(f"summation is {sum_}")
    file.write(f"subtract is {sub_}")