'''ASSIGNMENT-1'''
# IF STATEMENT

#1.
num=10   
if num>0:
    print("Number is positive")

#2.
age=67
if age>=18:
    print("Eligible to vote")


#3.
num=int(input("Enter the num:"))
if num%7==0:
    print("number is divisible")


#4.
marks=90
if marks>40:
    print("Pass")


#5.
num=int(input("Enter the num:"))
if num>100:
    print("Number is greater")


#6.
temp=56
if temp>45:
    print("Temp exceeds")



#7.
s=(input("Enter the string:"))
if len(s)>8:
      print("Length is more than 8 chr")


#8.
a=(input("Enter the password:"))
if a== "admin123":
    print("Logged In")


#9.
num=int(input("Enter the num:"))
if num%10==0:
    print("Number is a multiple of 10")


#10.
bal=1500
min_bal=2000
if bal<min_bal:
    print("Low limit")



#IF-ELSE STATEMENT


#11.
num=int(input("Enter the number:"))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")


#12.
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
if a>b:
    print("a is largest")
else:
    print("b is largest")



#13.
age=int(input("Enter your age:"))
if age>=18:
    print("Eligible for license")
else:
    print("Not eligible")


#14.
marks=int(input("Enter your marks:"))
if marks>=33:
          print("Pass")
else:
    print("Fail")



#15.
num=int(input("Enter your number:"))
if num>0:
    print("Positive")
else:
    print("Negative")


#16.
char=(input("Enter the char:"))
if char in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")


#17.
year=int(input("Enter the year:"))
if year%4==0:
    print("Leap year")
else:
    print("Not a leap year")


#18.
a=int(input("Enter the pass:"))
if a==123456:
    print("Valid password")
else:
    print("Invalid pass word")


#19.
salary=int(input("Enter your salary per month:"))
if salary>10000:
    print("Taxable")
else:
    print("Not taxable")


#20.
num=int(input("Enter your number:"))
if num>50:
    print("Greater")
else:
    print("Not greater")


#NESTED IF-ELSE

#21.
a=200
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
        print(c)


#22.
num=int(input("Enter the number:"))
if num>0:
    print("Positive number")
else:
    if num<0:
        print("Negative number")
    else:
        print("Number is zero")


#23.
marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
else:
    if marks>=75:
        print("Grade B")
    else:
        if marks>=60:
            print("Grade C")
        else:
            print("Fail")


#24.
a=int(input("Enter side 1:"))
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
                print("Scalene triangle")



#25.
char=(input("Enter the char:"))
if char>='A' and char<='Z':
    print("Uppercase")
else:
    if char>='a' and char<='z':
        print("Lowercase")
    else:
        if char>='0' and char<='9':
            print("Digit")
        else:
            print("Specialcharacter")


#26.
service= 250
unit=int(input("Enter unit consumption:"))
if unit<=100:
    bill=unit*5
else:
    if unit<=200:
        bill=unit*7
    else:
        bill=unit*10
bill=bill+service
print("Bill:",bill)


#27.
username=input("Enter username:")
password=input("Enter password:")
if username== "tanu":
    if password=="tanu@#12":
        print("Login successful")
    else:
        print("Incorrect usrename")
else:
    print("Incorrect password")

    
        
#28.
hindi=int(input("Enter your hindi marks:"))
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
    print("Fail")


#29.
a=100
b=200
c=30
if a>b:
    if a<c:
        print("Second largest:",a)
    else:
        if b>c:
            print("Second largest:",b)
        else:
            print("Second largest:",c)
else:
    if b<c:
        print("SEcond largest:",b)
    else:
        if a>c:
            print("Second largest:",a)
        else:
            print("Second largest:",c)


#30.
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



#ELIF CONDITION

#31.
day=int(input("Enter the day number from 1 to 7:"))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("You entered a wrong number")



#32.
month=int(input("Enter the month number from 1 to 12:"))
if month==1:
    print("January")
elif month==2:
    print("February")
elif month==3:
    print("March")
elif month==4:
    print("April")
elif month==5:
    print("May")
elif month==6:
    print("June")
elif month==7:
    print("July")
elif month==8:
    print("August")
elif month==9:
    print("September")
elif month==10:
    print("October")
elif month==11:
    print("November")
elif month==12:
    print("December")
else:
    print("You entered a wrong number")



#33.
per=input("Enter your percentage:")
if per>=90:
    print("A grade")
elif per>=75:
    print("B grade")
elif per>=60:
    print("C grade")
elif per>=50:
    print("D grade")
else:
    print("Fail")



#35.
signal=input("Enter your signal color :")
if signal=="red":
    print("Stop")
elif signal=="yellow":
    print("Get ready")
elif signal=="Green":
    print("Go")
else:
    print("Invalid color")


#36.
temp=float(input("Enter the temperature:"))
if temp<15:
    print("Cold")
elif temp<=30:
    print("Warm")
else:
    print("Hot")


#37.
salary=float(input("Enter employee salary:"))
if salary<20000:
    print("Low salary")
elif salary<=50000:
    print("Medium salary")
else:
    print("High salary")


#39.
num=int(input("Enter a number:"))
if num>=0 and num <=10:
    print("Singlr digit")
elif num<100:
    print("Double digit")
elif num<1000:
    print("Triple digit")
else:
    print("Multi digit")



#40.
marks=float(input("Enter your marks:"))
if marks<30:
    print("Poor - Rating: 1")
elif marks<=50:
    print("Average - Rating: 2")
elif marks<=80:
    print("Good - Rating: 3")
else:
    print("Excellent - Rating 4")



'''COMPLEX CONDITION'''

#41.
num=float(input("Enter your number:"))
if num%5==0 and num%11==0:
    print("Number is divisible")
else:
    print("Number is not divisible")


#42.
age=float(input("Enter your age:"))
salary=float(input("Enter your salary:"))
score=float(input("Enter your credit score:"))
if age>=21 and salary>=25000 and score>=700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


#43.
username=input("Enter your name:")
pass=input("Enter your password:")
if username=="tanu" and pass=="tanu124":
    print("Login successfully")
else:
    print("Not able to login")



#44.
marks=float(input("Enter your all subject marks:"))
average=float(input("Enter average:"))
if marks >=40 and average>=50:
    print("Pass")
else:
    print("Fail")



#45.
num=float(input("Enter number:"))
if num>=10 and num<=100:
    print("Number lies")
else:
    print("Not lies")



#46.
atten=float(input("Enter your attendance:"))
medical=input("Enter your medical certificate (Yes/No):")
if atten>=75% or medical=="yes":
    print("Allow to sit in exam")
else:
    print("Not allow")


#48.
email=input("Enter an e-mail:")
if '@' in email and '.' in email:
    print("Valid email:" , email)
else:
    print("Invalid email")


#49.
age=float(input("Enter your age:"))
health=input("Enter your health (good/bad):")
income=int(input("Enter your income:"))
if age>=25 and age<=60 and health=="good" and income<=30000:
    print("Available for insurance")
else:
    print("Not available")


#50.
year=int(input("Enter the year:"))
if (year%4==0)and (year%100!=0):
    print("Leap year")
else:
    print("Not a leap year")



'''INTERVIEW LEVEL QUESTION'''


#51.
service= 250
unit=int(input("Enter unit consumption:"))
if unit<=100:
    bill=unit*5
elif unit<=200:
    bill= bill = (100 * 5) + (unit - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (unit - 200) * 10

bill=bill+service

print("Bill:",bill)


#52.
bal=2763
print("1. check balance/n2 . withdrawl balance/n3 . Exit")
ch=int(input("Enter your choice:"))
if ch==1:
    print("Your current balance:",bal)
elif ch==2:
    w=int(input("Enter amount to withdrawl:"))
    if  w<=bal:
        print("Balance withdrawl")
        print("Remaining amount:",(bal-w))
    else:
        print("Insufficient balance")
else:
    print("Bye-Bye")


#53.
exp = int(input("Enter your experience:"))
performance=input("Enter your performance (good/average/poor):")
if exp>=5 and performance=="good":
    print("Promoted")
else:
    print("Not promoted")


#54.
marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Fail")


#55.
password = input("Enter password: ")

if(len(password)>=8 and
    any(c.isdigit() for c in password) and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password)):

    print("Strong Password")
else:
    print("Weak Password")


#56.
location=input("Enter location (local/outstation): ")
amount=float(input("Enter order amount: "))

if location.lower()=="local":
    if amount>=500:
        charge=0
    else:
        charge=50
else:
    if amount>=1000:
        charge=0
    else:
        charge=100

print("Delivery Charge:",charge)


#57.
attendance=int(input("Enter attendance %: "))
marks=int(input("Enter test marks: "))

if attendance>=75 and marks>=40:
    print("Eligible for Online Exam")
else:
    print("Not Eligible")



#59.
balance=float(input("Enter your account balance:"))
if balance<100000:
    print("Basic account")
elif balance<=50000:
    print("Saving account")
else:
    print("Premium account")



    

