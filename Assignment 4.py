'''LIST'''

#1.
a=[32,46,93,88,40]
print(a)


#2.
li=[10,20,30,40]
total=0
for i in lst:
    total+=i
avg=total/len(lst)
print("Sum:", total)
print("Average:", avg)


#3.
lst=[10, 5, 30, 2, 50]

largest=lst[0]
smallest=lst[0]
for i in lst:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largest:", largest)
print("Smallest:", smallest)



#4.
li=[1, 2, 3, 4, 5]
count = 0
for i in li:
    count += 1
print("Total elements:", count)


#5.
li=[1, 2, 3, 4, 5]
rev=[]
for i in range(len(li)-1, -1, -1):
    rev.append(lst[i])
print("Reversed list:", rev)


#6.
li=[10, 20, 30, 40]
ele = int(input("Enter element: "))
if ele in li:
    print("Element exists")
else:
    print("Element not found")


#7.
li=[1, 2, 2, 3, 4, 3, 5]
unique=[]
for i in lst:
    if i not in unique:
        unique.append(i)
print("List without duplicates:", unique)


#8.Ascending
li=[5, 2, 8, 1, 3]
for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
print("Ascending:", li)


#Descending
lst = [5, 2, 8, 1, 3]
for i in range(len(lst)):
    for j in range(i+1, len(li)):
        if li[i]<li[j]:
            li[i],li[j]=li[j],li[i]
print("Descending:", li)


#9.
l1 = [1, 2, 3]
l2 = [3, 4, 5]
merged = l1 + l2
result = []
for i in merged:
    if i not in result:
        result.append(i)

print("Merged without duplicates:", result)


#10.
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
common=[]
for i in l1:
    if i in l2 and i not in common:
        common.append(i)
print("Common elements:", common)


#11.
li=[1, 2, 3, 4, 5, 6]
even=[]
odd=[]
for i in lst:
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:", even)
print("Odd numbers:", odd)


#12.
li=[1,2,3,4,5,6,7,8,9,10]
print(li)
n=int(input("No. of right rotation:"))
for i in range(n):
    val=li.pop(len(li)-1)
    li.insert(0,val)
print(li)


#13.
li=[10, 20, 5, 40, 30]
largest = second = -999999
for i in lst:
    if i > largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print("Second largest:", second)

#14.
li=[[12,34,57],[5,6,89],59,60,[45,78,67]]
f_li=[]
print("Nested list:",li)
for x in li:
    if type(x)==list:
        for i in x:
            f_li.append(i)
    else:
        f_li.append(x)
print("Flaten list:",f_li)


#15.
li=[1, 2, 2, 3, 3, 3, 4]
freq={}
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Frequency:", freq)


#16.
li=[1, -2, 3, -4, 5]
for i in range(len(li)):
    if lst[i] < 0:
        lst[i] = 0
print("Updated list:", li)


#17.
li = [1, 2, 3, 2, 4, 2, 5]
ele = int(input("Enter element to remove: "))
result = []
for i in li:
    if i != ele:
        result.append(i)
print("Updated list:", result)


#18.
li=[1, 2, 3, 2, 1]

if li==li[::-1]:
    print("List is palindrome")
else:
    print("List is not palindrome")



#19.
li=[2,4,6,10,12,14,18]
diff=li[1]-li[0]
for i in range(0,len(li)-1):
    if li[i]+diff!=li[i+1]:
        print(f"{i+2} Place missing value:",li[i]+diff)



#20.
l1=[1, 2, 3]
l2=[4, 5, 6]
result = []
for i in range(len(l1)):
    result.append(l1[i] + l2[i])
print("Result:",result)



#21.
li = [21,78,89,765,23,23,35,39,45,667,8,9,635]
longest=[]
temp=[li[0]]

for i in range(1, len(li)):
    if li[i]>li[i-1]:
        temp.append(li[i])
    else:
        if len(temp)>len(longest):
            longest=temp.copy()
            temp=[li[i]]
            if len(temp)>len(longest):
                    longest=temp.copy()

print(longest)



#22.
li=[1,4,6,54,3,1,34,6,5,3,2,1,3,4,6,54]
group=[]
selected=[]
for x in li:
    if x not in selected:
        selected.append(x)
        for j in li:
            if x==j:
                group.append(j)
print(group)



'''TUPLE'''


#23.
t=(1,45,67,89,22,56)
print(t)



#24.
t=(23,45,88,90,72)
print(len(t))


#25.
t=(12,22,56,86,66,74,15)
print(max(t))
print(min(t))


#26.
t=(89,67,45,33,12)
l=list(t)
print(l)


#27.
t=(0,1,2,4,5)
ele=int(input("Enter your element:"))
if ele in t:
    print("Element exists")
else:
    print("Element not exists")



#28.
t=(6,7,4,9,6,3,7,2,1,6,6,3,4)
ele=int(input("Enter element:"))
count=0
for i in t:
    if i==ele:
        count=count+1
print(count)

'''OR'''

t=(6,7,4,9,6,3,7,2,1,6,6,3,4)
ele=int(input("Enter element:"))
print(t.count(ele))



#29.
a=("Aman", "kumar","Tanu","Anchal")
print(a[0:2])


#30.
t=(5,8,0,0,7,8,6,5,1)
repeated=[]
for i in t:
    if t.count(i)>1 and i not in repeated:
        repeated.append(i)
print(repeated)



#31.
t1=(1,2,3)
t2=(8,5,7)
merged = t1+t2
print("Merged tuple:,merged)


#32.
t=(10,20,30)
a,b,c = t
print("a=",a)
print("b=",b)
print("c=",c)



#33.
t=(5,7,2,5,9)
sorted_tuple=tuple(sorted(t))
print("Sorted tuple:",sorted)


#34.
li=[("a",1),("b",2),("c",3)]
d=dict(li)
print("Dictionary:",d)


#35.
t=(10,30,40,60)
ele=int(input("Enter element:"))
if ele in t:
      print("Index of element:",t.element(ele))
else:
    print("Element not found")



#36.
t1=(23,45,67,8,90)
num=67
l=[]
for x in t1:
    if x!=num:
        l.append(x)
print(tuple(l))


#37.
t1=(1,3,4,7,8)
t2=(5,7,2,6,0)
common=[]
for i in t1:
    if i in t2 and i not in common:
        common.append(i)
print("Common elements:",tuple(common))



#38.
t=(1,2,3,4,5)
if t==t[::-1]:  #reverse the tuple
    print("Tuple is palidrome")
else:
    print("Tuple is not palidrome")



#39.
t=(1,5,5,78,94,653,2,4,6,78,6,5,3,45,6,7,56,44)
max=t.count(t[0])
ele=t[0]
for m in t:
    if max<t.count(m):
        max=t.count(m)
        ele=m
print(ele,max)


#40.
t=((3,4,5),(6,7,8),(0,9,1))
print(t[0])
print(t[1])
print(t[2])








