'''LAMBDA BASICS'''

#1.

add=lambda a,b:a+b
print(add(30,40))


#2.

check_even=lambda num:"Even" if num%2==0 else "odd"
print(check_even(8))


'''MAP'''

#1.

square=lambda val:val**2
li=[1,2,3,4,5,6,7,8,9,10]
print(list(map(square,li)))


#2.

li=["tanushree","harsh","manan","vedant"]
result=list(map(lambda x:x.upper(),li))
print(result)



'''FILTER'''

#1.

li=[3,5,7,8,6,0,3,4,2]
check_even=lambda num:True if num%2==0 else False
print(list(filter(check_even,li)))


#2.

li=["Nature","Harsh","Manan","Shruti","Yachana"]
check_words=lambda x:True if len (x)>5 else False
print(list(filter(check_words,li)))


'''REDUCE'''

#1.

from functools import reduce
li=[1,2,3,4,5,6,7,8,9,10]
add=lambda a,b:a+b
print(reduce(add,li))


#2.

from functools import reduce
li=[1,2,3,4,5,6,6,7,7,8]
mul=lambda a,b:a*b
print(reduce(mul,li))



'''INTERMEDIATE LEVEL'''


#5.

li=[2,3,4,6,7,8]
result=list(map(lambda num:num*10,li))
print(result)


#6.

li=[20,45,15,10,60,44]
result=list(filter(lambda num: True if num%3==0 else False,li))
print(result)


#7.

from functools import reduce
li=[5,9,0,7,8,3,5,2,1]
max_num=reduce(lambda a,b: a if a>b else b,li)
print(max_num)


#8.

li=["aman","radha","anchal","vibhu","tushar"]
result=list(map(lambda name:name.capitalize(),li))
print(result)


#9.

li=["madam","python","level","code","radar","hello"]
result=list(filter(lambda word:word==word[::-1],li))
print(result)




