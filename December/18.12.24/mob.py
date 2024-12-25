# def outer():
#     n = 5
#     def inner():
#         nonlocal n
#         n += 1
#         print(n)
#     return inner
# fn = outer()
# fn()
# fn()
# fn()

# def coffe(typeCoffe):
#     def sizeCoffe(size):
#         return f"Ваш заказ: {size} {typeCoffe}"
#     return sizeCoffe

# latte = coffe("Латте")
# capuchino = coffe("Капучино")

# print(latte("Большой"))
# print(capuchino("Средний"))

# def outFunc():
#     num = 5

#     def inputFunc():
#         nonlocal num
#         print("Внутри внутренней функции:", num)
#     inputFunc()
#     print("Внутри внешней функции:", num)

# outFunc()

# def passanger_counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count
    
#     return increment

# turnstile = passanger_counter()
# print(turnstile())
# print(turnstile())
# print(turnstile())

# def user(name):
#     def inner():
#         print(f"Привет, {name}!")
#     return inner
# user_greet = user("Тим")
# user_greet()
# user_greet = user("Мит")
# user_greet()

# def attention(text):
#     def inner():
#         print(f"Внимание, {text}")
#     return inner
# a = attention("Пора пить")
# a()
# a = attention("Пора есть")
# a()