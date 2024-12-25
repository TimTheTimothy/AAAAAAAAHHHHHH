# def boom():
#     a = int(input())
#     b = int(input())
#     print("Equals =",a+b)

# boom()

def count():
    product = 1
    while True:
        number = int(input("Insert a number untill you insert 0- "))
        if number == 0:
            break
        product *= number
    return product

print(count())