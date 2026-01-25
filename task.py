Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
p=float(input("enter principal amount: "))
enter principal amount: 25
r=float(input("enter rate of interest: "))
enter rate of interest: 14
t=float(input("enter time (in year): "))
enter time (in year): 5
si=(p*r*t)/100
print("simple interest= ",si)
simple interest=  17.5

a=int(input("enter the first number: "))
enter the first number: 14
b=int(input("enter the second number: "))
enter the second number: 5
print("maximum number is: ",max(a,b))
maximum number is:  14

for i in range(1,6):
    print(i)

    
1
2
3
4
5

text=input("enter a string: ")
enter a string: radhe krushn
length=len(text)
print("length of the string= ",length)
length of the string=  12

print("welcome to python programming!")
welcome to python programming!

text=input("enter a string: ")
enter a string: Radhe
print("first character is: ",text[0])
first character is:  R

text=input("enter a string: ")
enter a string: krushn
print("last character is: ",text[-1])
last character is:  n

num=int(input("enter a number: "))
enter a number: 7
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
... else:
...     print("number is zero")
... 
...     
number is positive
>>> 
>>> a=int(input("enter first number: "))
enter first number: 14
>>> b=int(input("enter second number: "))
enter second number: 25
>>> c=int(input("enter third number: "))
enter third number: 07
>>> sum=a+b+c
>>> print("sum of three number= ",sum)
sum of three number=  46
>>> 
>>> name=input("enter your name: ")
enter your name: drashti
>>> print("Radhe radhe",drashti)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print("Radhe radhe",drashti)
NameError: name 'drashti' is not defined
>>> print("radhe radhe",name)
radhe radhe drashti
