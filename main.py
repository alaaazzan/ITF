# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
#print ("Alaa")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#print("Ali")
#if 10 > 2:
 #   print ("Yes")

#print ("no")
#TODO Tsak

#print ("Enter num1")
#input("Enter num1 =")
#age=True
#age=int(age)
#print (age)
#print(type(age))


#my_name=None
##num1=input("Enter num1 = ")
#num2=input("Enter num2 = ")
#print (num1,num2)
#print (type(age))

#first_name=input("Enter first name : ")
#last_name=input("Enter last name : ")
#paragraph=f"""
#>>>name : {first_name} {last_name}
#1_nationality is palestainian

#"""
#print (paragraph)

x="  Hello World         "
#print (x[2:-2])
#print (x.upper())
#print (x.lower())
#print (x.title())
#print (len(x))
#print (x.strip())
#print (x.replace("l","*"))
#print (x.replace(x[2:-2]))
#print (x.split())
#x="Alaa"
#y=5

#print("m"not in x)


# def my_function():
#   print("Hello from a function")
#
# my_function()
# i=0
# counter=0
# while True:
#     if i>100:
#         break
#
#     counter+=i
#     i+=1
# print(counter)


# def g (avg):
#     if avg>=90:
#         return "E"
#     elif avg>=80:
#         return "g"
#     else:
#         return "F"




# mark_count =int(input("Enter num of marks = "))
# total =0
# for i in range (mark_count):
#     mark=int (input("Enter mark = "))
#     total+=mark
#
# avg = total/mark_count
# print(avg)
# print(g(avg))
# total=0
my_list =[10,20,30]
new=[0,1,2]
# for i in my_list:
#     total+=i
# print(total)
#
# print(sum(my_list))
# my_list.insert(0,10)
# my_list.extend(new)
# my_list.pop()
# my_list.append(10)


# my_list.sort()
# my_list.reverse()
# my_list.sort(reverse=True)
# my_list.remove(20)
print(type(my_list))



# print(max(my_list))

# max_num =my_list[0]
# for i in my_list:
#     if i> max_num:
#         max_num=my_list[i]
#
# print(max_num)
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
    print("Hello, choose the operation you want:")
    print(
        "1. Sum\n2. Subtract\n3. Multiply\n4. Division\n5. Calculate triangle area\n6. Calculate circle area\n7. Calculate rectangle area\n8. Exit")

    choice = int(input("Your choice: "))

    if choice == 8:
        break
    elif choice == 2:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        sub(num1, num2)
    elif choice == 3:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        mul(num1, num2)
    elif choice == 4:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        div(num1, num2)
    elif choice == 5:
        Base = int(input("Enter Base: "))
        lengthint=(input("Enter Base: "))
