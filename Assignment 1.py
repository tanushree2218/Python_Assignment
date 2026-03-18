'''ASSIGNMENT-1'''

'''IF STATEMENT'''

'''num=10
if num>0:
    print("Number is positive")'''

'''age=67
if age>=18:
    print("Eligible to vote")'''

'''num=int(input("Enter the num:"))
if num%7==0:
    print("number is divisible")'''

'''marks=90
if marks>40:
    print("Pass")'''

'''num=int(input("Enter the num:"))
if num>100:
    print("Number is greater")'''

'''temp=56
if temp>45:
    print("Temp exceeds")'''

'''s=(input("Enter the string:"))
if len(s)>8:
      print("Length is more than 8 chr")'''


'''a=(input("Enter the password:"))
if a== "admin123":
    print("Logged In")'''


'''num=int(input("Enter the num:"))
if num%10==0:
    print("Number is a multiple of 10")'''


'''bal=1500
min_bal=2000
if bal<min_bal:
    print("Low limit")'''



'''IF-ELSE STATEMENT'''

'''num=int(input("Enter the number:"))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")'''


'''a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
if a>b:
    print("a is largest")
else:
    print("b is largest")'''


'''age=int(input("Enter your age:"))
if age>=18:
    print("Eligible for license")
else:
    print("Not eligible")'''


'''marks=int(input("Enter your marks:"))
if marks>=33:
          print("Pass")
else:
    print("Fail")'''


'''num=int(input("Enter your number:"))
if num>0:
    print("Positive")
else:
    print("Negative")'''


'''char=(input("Enter the char:"))
if char in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")'''


'''year=int(input("Enter the year:"))
if year%4==0:
    print("Leap year")
else:
    print("Not a leap year")'''


'''a=int(input("Enter the pass:"))
if a==123456:
    print("Valid password")
else:
    print("Invalid pass word")'''


'''salary=int(input("Enter your salary per month:"))
if salary>10000:
    print("Taxable")
else:
    print("Not taxable")'''

'''num=int(input("Enter your number:"))
if num>50:
    print("Greater")
else:
    print("Not greater")'''


''' NESTED IF-ELSE '''

'''a=200
b=60
c=500
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)'''


'''num=int(input("Enter the number:"))
if num>0:
    print("Positive number")
else:
    if num<0:
        print("Negative number")
    else:
        print("Number is zero")'''


'''marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
else:
    if marks>=75:
        print("Grade B")
    else:
        if marks>=60:
            print("Grade C")
        else:
            print("Fail")'''



'''a=int(input("Enter side 1:"))
b=int(input("Enter side 2:"))
c=int(input("Enter side 3:"))
if a==b:
    if b==c:
        print("Equilateral triangle")
    else:
        print("Isoceles triangle")
else:
    if b==c:
        print("Isoceles triangle")
    else:
        if a==c:
            print("Isoceles triangle")
        else:
                print("Scalene triangle")'''



'''char=(input("Enter the char:"))
if char>='A' and char<='Z':
    print("Uppercase")
else:
    if char>='a' and char<='z':
        print("Lowercase")
    else:
        if char>='0' and char<='9':
            print("Digit")
        else:
            print("Specialcharacter")'''


'''username=input("Enter username:")
password=input("Enter password:")
if username== "tanu":
    if password=="tanu@#12":
        print("Login successful")
    else:
        print("Incorrect usrename")
else:
    print("Incorrect password")'''

    
        
'''hindi=int(input("Enter your hindi marks:"))
english=int(input("Enter your english marks:"))
maths=int(input("Enter your maths marks:"))
if hindi<=40:
    if english<=30:
        if maths<=33:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Fail")
else:
    print("Fail")'''



age=int(input("Enter your age:"))
salary=int(input("Enter your salary:"))
credit=int(input("Enter your credit score:"))
if age>=21 and age<=40:
    if salary>=200000:
        if credit>=700:
            print("Eligible for loan")
        else:
            print("Not eligible (Low credit score)")
    else:
        print("Not eligible (Low salary)")
else:
    print("Not eligible (Invalid age)")
