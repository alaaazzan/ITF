def sum (num1,num2):
    total=num1+num2
    print(total)

def sub (num1,num2):
    total=num1-num2
    print(total)

def mul (num1,num2):
    total=num1*num2
    print(total)

def div (num1,num2):
    total=num1/num2
    print(total)

def triangle (num1,num2):
    total=(num1*num2)/2
    print(total)

def circle (R):
    total=3.14*R*R
    print(total)

def rectangle (num1,num2):
    total=num1*num2
    print(total)

while True:
    print("Hello,choose the operation you want:\n1. Sum\n2. Subtract\n3. Multiply\n4. Division\n5. Calculate triangle area\n6. Calculate circle area\n7. Calculate rectangle area\n8. Exit")
    choice =int(input ("-Your choice : "))
    if choice==8:
        break
    elif choice==1:
        num1 = int(input("Enter num1 = "))
        num2 = int(input("Enter num2 = "))
        sum(num1, num2)
    elif choice == 2:
        num1 = int(input("Enter num1 = "))
        num2 = int(input("Enter num2 = "))
        sub(num1, num2)
    elif choice == 3:
        num1 = int(input("Enter num1 = "))
        num2 = int(input("Enter num2 = "))
        mul(num1, num2)
    elif choice == 4:
        num1 = int(input("Enter num1 = "))
        num2 = int(input("Enter num2 = "))
        div(num1, num2)
    elif choice == 5:
        Base = int(input("Enter Base = "))
        length = int(input("Enter length = "))
        triangle(Base, length)
    elif choice == 6:
        Radius = int(input("Enter Radius = "))
        circle(Radius)
    elif choice==7:
        Length = int(input("Enter Length = "))
        width = int(input("Enter width = "))
        rectangle(Length, width)
