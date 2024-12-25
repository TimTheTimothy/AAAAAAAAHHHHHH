# 1
# try:
#     x = 10 / 0
#     print(x)
# except ZeroDivisionError:
#     print("Error, the number is being divided by zero")

# 2
# try:
#     a = int(input("Insert a number: "))
#     print(a)
# except ValueError:
#     print("Error, insert a number, not a symbol")

# 3
# a = [1,5,6]
# try:
#     x = a[3]
#     print(x)
# except IndexError:
#     print("Error, this index is not in the range")

# 4
# g = {"a":2,"b":4}
# try:
#     x = g["c"]
#     print(x)
# except KeyError:
#     print("Error, the key dose not exist")

# 5
try:
    a = int(input("Insert the first number: "))
    b = int(input("Insert the second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Error, the number is being divided by zero")