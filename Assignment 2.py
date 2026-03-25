'''FOR LOOP'''


#1.
for i in range(1,11):
    print(i)
    

#2.
for i in range(1,21):
    if i%2==0:
        print(i)


#3.
total=0
for i in range(1,11):
    total=total+i
print("Sum=",total)


#4.
num=int(input("Enter your number:"))
for i in range(1,11):
    multiply=num*i
    print(num, "x", i, "=", multiply)


#5.
st="HELLO WORLD"
count=0
for i in st:
    count+=1
print("Total characters:",count)


#6.
for i in range(1,11):
    if i==5:
        break
    print(i)


#7.
numbers=list(range(1,26))
for i in numbers:
    if i==25:
        print("Found")
        break


#8.
numbers=list(range(-1,-10 ,-1))
for i in numbers:
    if i<0:
        print(i)
        break


#9.
for i in range(1,11):
    if i==5:
        continue
    print(i)


#10.
for i in range(1,21):
    if i%2==0:
        continue
    print(i)


#11.
text="PYTHON"
for ch in text:
    if ch=='O':
        continue
    print(ch)


#12.
for i in range(1,6):
    pass


#13.
'''for i in range(1,11):
    if i==6:
        pass
    print(i)'''


#14.
for i in range(1,11):
    if i==6:
        continue
    print(i)


#15.
num=[10,20,30,40,50]
for i in num:
    if i==100:
        print("Found")
        break
else:
    print("Not found")



#16.
num=int(input("Enter your number:"))
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("Prime")



#17.
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


#18.
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#19.
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

#20.
for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ", end="")
    print()


#21.
k=0
for i in range(9,0,-2):
    print(" "*k,end="")
    k=k+1
    for j in range(1,i+1):
        print("*",end=" ")
    print()


