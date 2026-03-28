'''WHILE LOOP'''

#1.
a=1
while a<=10:
    print(a)
    a=a+1


#2.
a=1
while a<=20:
    if a%2==0:
        print(a)
    a=a+1


#3.
a=1
while a<=20:
    if a%2!=0:
        print(a)
    a=a+1



#4.
a=10
while a>=1:
    print(a)
    a=a-1


#5.
i=1
while i<=10:
    print("5 x", i, "=",5 * i)
    i=i+1


#6.
num=1
add=0
while num<=10:
    add=add+num
    num=num+1
print("Addition:", add)


#7.
num=int(input("Enter your number:"))
fact=1
while num>1:
    fact=fact*num
    num=num-1
print("Fctorial:",fact)


#8.
num=int(input("Enter a number:"))
count=0
while num>0:
    num=num//10
    count=count+1
print("Number of digits:",count)


#9.
num=6783
while num>0:
    rem=a%10
    add=add*10+rem
    num=num//10
print("Reverse of a num :")


#10.
num=int(input("Enter a num:"))
original=num
reverse=0

while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
if original==reverse:
    print("Palidrome")
else:
    print("Not Palidrome")
    

#11.
i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1


#12.
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1


#13.
correct_pass="tanu123"
user_pass=""
while user_pass!=correct_pass:
    user_pass=input("Enter password:")
print("Access granted")


#14.

import random
num = random.randint(1, 10)
while True:
    guess=int(input("Guess the number (1-10): "))
    if guess<secret:
        print("Too low")
    elif guess>secret:
        print("Too high")
    else:
        print("Correct Guess")
        break


#15.
while true:
    num=int(input("Enter your num (0 for exit):"))
    add=add+num
    if num==0:
        break
print("Total",add)


#16.
a=0
b=1
i=1
terms=int(input("Enter your terms:"))
while i<=terms:
    print(a)
    c=a+b
    a=b
    b=c
    i=i+1



#17.
num=int(input("Enter your number:"))
copy=num
add=0
while num>0:
    rem=num%10
    add=add+rem**3
    num=num//10
print("New number:",add)
if copy==add:
    print("Amstrong")
else:
    print("Not armstrong")



#18.
num = 1
while num <= 50:
    i = 1
    count = 0

    if num > 1:
        while i <= num:
            if num % i == 0:
                count = count + 1
            i = i + 1

        if count == 2:
            print(num)

    num = num + 1
    

