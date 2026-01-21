def divide_single(x,y):
    return x/y
def divide_multiple(x,**y):
    lists = y.split(" ")
    product = 1 
    listn = [int(i) for i in lists]
    for i in listn:
        product = product * i 
    return x/product


print("do you want to divide one number by the other or divide a number by multiple numbers?")
a = int(input("1.single or 2.multiple ,  tell by entering the integer "))
if a == 1 :
    number1 = int(input("number:"))
    number2 = int(input("by :"))
    print(divide_single(number1,number2))
else

