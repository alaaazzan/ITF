# def add(x,y):
#     total=x+y
#     print(total)
#
# add (10,5)
#
# def sub(x,y):
#     total=x-y
#     print(total)
#
# sub (10,5)
#
#
# def div(x,y):
#     total=x//y
#     print(total)
#
# div (10,5)
#
# def mul(x,y):
#     total=x*y
#     print(total)
#
# mul (10,5)


# my_num=int(input(("Enter num = ")))
# if my_num%2==0 and my_num !=0:
#     print (f"{my_num} is even")
# elif my_num==0:
#     print("0")
# else:
#     print(f"{my_num} is odd")

# counter =0
# max_num=10
# if counter<max_num:
#     print(counter)
#
# counter+=1

#
# for i in range(0,10):
#     print ("school")

# for i in "Ahmad":
#     print(i)
# num=int(input("Enter num = "))
# for i in range(0,13):
#     print(f"{i}*{num}={i*num}")

# for i in range (0,11):
#     print(i)

# for i in range(0,13):
#    # print(f"****{i}****")
#    for j in range(0,13):
#        print (f"{i}*{j}={i*j}")


# x=0
# for i in range(0,101):
#     if i%2==0:
#        x+=i
# print(x)
i=0
counter=0
while True:
    if i>100:
        break

counter+=i
i+=1
print(counter)


print("Hello,choose the operation you want:\n1. Sum\n2. Subtract\n3. Multiply\n4. Division\n5. Calculate triangle area\n6. Calculate circle area\n7. Calculate rectangle area\n8. Exit")
choice =int(input ("-Your choice : "))
if choice==1:
    num1=int(input("Enter num1 = "))
    num2= int(input("Enter num2 = "))
    sum(num1,num2)
elif choice==2:
    num1 = int(input("Enter num1 = "))
    num2 = int(input("Enter num2 = "))
    sub(num1,num2)
elif choice==3:
    num1 = int(input("Enter num1 = "))
    num2 = int(input("Enter num2 = "))
    mul(num1,num2)
elif choice==4:
    num1 = int(input("Enter num1 = "))
    num2 = int(input("Enter num2 = "))
    div(num1,num2)
elif choice==5:
    Base = int(input("Enter Base = "))
    length = int(input("Enter length = "))
    triangle(Base,length)
elif choice==6:
    Radius = int(input("Enter Radius = "))
    circle(Radius)
elif choice==7:
    Length = int(input("Enter Length = "))
    width = int(input("Enter width = "))
    triangle(Length,width)
# elif choice==8:



