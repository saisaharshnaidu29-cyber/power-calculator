print("type an power and i will calculate using loops")
base = int(input("base: "))
exponent = int(input("exponent: "))
result = 1
for i in range(exponent):
    result *= base
print(f"{base} to the power of {exponent} is {result}")
print("the answer is :", result)