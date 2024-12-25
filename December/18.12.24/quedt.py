# 1
# import random
# c = []
# i = 0
# while i <10:
#     c.append(random.randint(0,100))
#     i += 1
# print(c)

# 2
# a = []
# print("Insert 10 numbers:")
# for i in range(1,11):
#     a = int(input(f"Number {i} "))  
#     a.append(a)
# sum = 0
# for i in a:
#     sum += i
# print("The list of numbers you inserted:", a)
# print("And all of them together:", sum)


# 3
# def stepper(step):
#     counter = 0
#     def closure():
#         nonlocal counter
#         counter += step
#         return counter
#     return closure
# f = stepper(2)
# print(f())
# print(f())

# 4
# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
# num = counter()
# print(num())
# print(num())
# print(num())

# 5
# a = [25,34,54,21,95,18,17,29]
# b = 0
# for i in a:
#     b += i
# print(b)