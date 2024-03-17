"""
1. 

Write a program to find the location of given char in the given string.
"""

string = input("enter your string: ")
char = input("enter only one letter to find it's location: ")
lst = list()
for i in range(len(string)):
    if char == string[i]:
        lst.append(i+1)
print("the location of {} is {}".format(char,lst))

"""
2. 

For a given number find out the equivalent Binary number.
"""

a = int(input("enter the number: ")) # 23
d = a
emt_str = ""
while(a!=0): 
    b = a//2  
    c = a-(b*2)
    emt_str = str(c) + emt_str 
    a = b
print("the binary from of %d is %s "%(d,emt_str))

"""
3. 

Suppose 3 sets A,B,C contains the integer numbers divisible by 2,3,5 respectively . for a given number find out the region in which it belongs to.
"""

a = int(input("enter a number: "))
if(a%2 == 0):
    print(a,"belongs to A")
else:
    print(a,"does not belongs to A")
if(a%3 == 0):
    print(a,"belongs to B")
else:
    print(a,"does not belongs to B")
if(a%5 == 0):
    print(a,"belongs to C")
else:
    print(a,"does not belongs to C")
    


"""
4. 

Take a number as input and reverse the number.
"""

a = int(input("enter the number: "))
b = a
sum = 0
while(a!=0):
    rem = a%10
    sum = (sum*10)+rem
    a = int(a/10)
print("the reversed number of",b,"is",sum)



"""
5. 
write a program to print this output above

  *
 * *
* * *
"""

a = int(input("enter the number: "))
s = " "
for i in range(1,a+1):
    print((a-i)*s,end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print(end="\n")



"""
6.

* * *
 * *
  *
"""
a = int(input("enter the number: "))
s = " "
for i in range(1,a+1):
    print((i-1)*s,end="")
    for j in range(0,(a-i)+1):
        print("*",end=" ")
    print(end="\n")


"""
7.

* * * *
* * *
* *
*
"""
row = int(input("enter the number: "))
for i in range(row,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
        if j==i:
            print(end="\n")


# we can do this also

r = int(input("enter the number: "))
for i in range(r,0,-1):
    print("*"*i)


"""
8.

*
* *
* * *
* * * *
"""

row = int(input("enter a number: \n")) 
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
        if j==i:
            print(end="\n")
  

# or we can use this,

a = int(input("enter the number: "))  
for i in range(1,a+1):
    print("*"*i)



"""
9.

1
0 1
1 0 1
0 1 0 1
"""
n = int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i%2 != 0):
            a = j%2
            print(a,end=" ")
        else:
            a = (j+1)%2
            print(a,end=" ")
    print(end="\n")


"""
10.

1
1 2 
1 2 3
1 2 3 4
"""
n = int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(end="\n")


"""
11.

1
2 3
4 5 6
7 8 9 10
"""
a = int(input("enter the number: "))
count = 0
for i in range(1,a+1):
    for j in range(1,i+1):
        count += 1
        print(count,end=" ")
    print(end="\n")