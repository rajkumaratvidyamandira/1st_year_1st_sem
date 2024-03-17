"""
1. to evaluate the area of different geometrical figures depending on user’s
choice, where figure may be one of the followings:-
a) a rectangle, where the value of the length and breadth are taken as
input. Area = length * breadth
b) a circle, where the value of radius be taken as input. Area = pi *
(radius)2 , where pi = 3.141592653589793 (otherwise, you may
use pie - by importing math library).
c) a triangle, where the measurement of three sides be a, b and c .
Values of a, b and c are taken as input.
Area = √s∗ (s−a )∗ (s −b )∗ (s−c ), where s=(a+b+c)/2
"""



import math

def area_tri(a,b,c):
    s = (a+b+c)/2 # half perimeter
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    # area = math.sqrt(a)
    return area

user_choice = True
while(user_choice):
    user_choice = input("\n\nenter your choice: \nto get the area of rectangle--1,\nto get the area of circle--2,\nto get the area of triangle--3,\nexit -- x: ")
    if user_choice == "1":
        #rectangle
        length = float(input("enter the value of length: "))
        breadth = float(input("enter the value of breadth: "))
        area = length * breadth
        print("the area of the rectangle is",area)
    elif user_choice == "2":
        # circle
        radius = float(input("enter the value of radius: "))
        area = math.pi * (radius**2)
        print("the area of the circle is",area)
    elif user_choice == "3":
        print("enter the value of three sides of the triangle:")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        if (a+b>c and a+c>b and c+b>a):
            print("the area of the triangle is",area_tri(a,b,c))
        else:
            print("triangle can not be created")
    else:
        user_choice = False



"""
2. to find out the value of addition, subtraction and production of two complex numbers.
"""

com_1 = 20+10j
com_2 = 10+5j

# addition
com_3 = com_1 +com_2
print("the addition of {} and {} is {}\n".format(com_1,com_2,com_3))

# substruction
com_4 = com_1 - com_2
print("the substraction of {} and {} is {}\n".format(com_1,com_2,com_4))

# multiplication
com_5 = com_1 * com_2
print("the multiplication of {} and {} is {}\n".format(com_1,com_2,com_5))

# division
com_5 = com_1 / com_2
print("the division of {} and {} is {}\n".format(com_1,com_2,com_5))




"""
3. To find out the sum or product or subtraction of two numbers depending on
the user’s choice. Suppose enter 1 for sum, or 2 for product, or 3 for subtraction.
"""

choice = int(input("enter which operation do you want to do\n 1 for sum , 2 for product , 3 for substraction , 4 for division:\n"))
if (choice>4):
    print("invalid input")
else:

    a = float(input("enter the 1st number: "))
    b = float(input("enter the 2nd number: "))

    if choice == 1:
        c = a+b
        print("the sum of {} and {} is {}".format(a,b,c))
    elif choice == 2:
        c = a*b
        print("the product of {} and {} is {}".format(a,b,c))
    elif choice == 3:
        c = a-b
        print("the substraction of {} and {} is {}".format(a,b,c))
    elif choice == 4:
        try:
            c = a/b
            print("the division of {} and {} is {}".format(a,b,c))
        except ZeroDivisionError:
            print("denominator as 0 , not allowed")
    else:
        print("invalid input")



"""
4. to find out the equivalent grade for a given marks(in percentage), where
grades are set as A++, A+, A and B respectively for marks greater or equal
to 80, marks greater or equal to70 but less than 80, marks greater or equal
to 60 but less than 70 and marks less than 60 . Value of marks be taken as input.
"""

mark = int(input("enter your mark in percentage: \n"))
if (mark > 100 or mark < 0):
    print("wrong input")
elif mark >= 80:
    print("your grade is A++")
elif (mark >= 70 and mark < 80):
    print("your grade is A+")
elif (mark >= 60 and mark < 70):
    print("your grade is A")
elif (mark < 60):
    print("your grade is B")


"""
5. to find the maximum and minimum value among three numbers taken as input.
"""

print("enter three number")
max = 0 ; min = 0
for i in range(3):
    a = int(input("enter: "))
    if i == 0:
        max = a ; min = a
    if a > max:
        max = a
    if a < min:
        min = a
print("the maximum value among the numbers is",max)
print("the minimum value among the numebrs is",min)


"""
6. to find the sum of the series (1/n!)
"""

def fact(n):
    if (n == 0):
        return 1
    else:
        f = 1
        for i in range(1,n+1):
            f *= i
        return f
    

n = int(input("enter the value of n in (1/n!) series: "))
sum = 0
for i in range(0,n+1):
    sum = sum+(1/fact(i))
print("the sum of the series 1/(n!) is",sum)

"""
7. to find the sum of the series (1/2^n )
"""

n = int(input("enter the value of n in (1/2^n) series: "))
sum = 0
for i in range(0,n+1):
    sum = sum+(1/(2**i))
print("the sum of the series 1/(2^n) is",sum)



"""
8. to check whether a given number is prime or not.
"""

import math
i = 0;

i = i+1
n = int(input("enter a number: "))
if (n == 0 or n == 1):
    print("%d is neither prime or non prime" %(n))
else:
    count = 0
    for i in range(1,int(math.sqrt(n))+1): 
        if n%i == 0:
            count += 1;
            if (count > 1):
                print("the number %d is not a prime." % (n))
                break
    if (count == 1 ):
        print("the number %d is prime" % (n))


"""
9. to find out all the prime numbers within a given range.
"""

import math

def prime(n):
    if (n == 0 or n == 1):
        return 2;
    else:
        count = 0
        for i in range(1,int(math.sqrt(n))+1): 
            if n%i == 0:
                count += 1;
                if (count > 1):
                    return 0
                    break
        if (count == 1 ):
            return 1

num = input("enter the range(a b): ")
a,b = num.split()
for i in range(int(a),int(b)+1):
    c = prime(i)
    if c == 1:
        print("%d is a prime number"%i)
    # elif c == 2:
    #     print("%d is neither prime or non prime"%i)
    # else:
    #     print("%d is not a prime"%i)


"""
10.To print first n fibonacci numbers. Output as:- Numbers are -> 0,1,1,2,3,5,8,...
"""

def fab(n):
    if n == 1:
        return 0
    elif (n == 2) or (n == 3):
        return 1
    else:
        return fab(n-2)+fab(n-1)
n = int(input("enter the number: "))

for i in range(1,n+1):
    print(fab(i),end=" ")



"""
11.To print nth fibonacci number.
"""

def feb(n):
    if (n==1):
        return 0
    elif (n == 2) or (n == 3):
        return 1
    else:
        return feb(n-2)+feb(n-1)
        
n = int(input("enter the number: "))
print("{}th fibonacci number is {}".format(n,feb(n)))


"""
12.to check whether the number is palindrome or not
"""

num = int(input("enter the number: "))
num_copy = num 
rev_num = 0
while(num!=0):
    rem = num%10
    num = num//10
    rev_num = (rev_num*10)+rem

if rev_num == num_copy:
    print("{} is palindrome".format(num_copy))
else:
    print("{} is not a palindrome".format(num_copy))
