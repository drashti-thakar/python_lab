Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#for loop

#print numbers from 1 to 10
for i in range(1,11):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
#print even numbers from 1 to 10
for i in range(1,11):
    if i%2==0:

        print(i)

        
2
4
6
8
10
#print odd numbers for 1 to 15
for i in range(1,16):
    if%2!=0:
        
SyntaxError: invalid syntax
if i%2!=0:
    print(i)

    
for i in range(1,16):
    if i%2!=0:
        print(i)

        
1
3
5
7
9
11
13
15
#print table of 14
for i in range(1,11):
    print("14 x",i,"=",14*i)

    
14 x 1 = 14
14 x 2 = 28
14 x 3 = 42
14 x 4 = 56
14 x 5 = 70
14 x 6 = 84
14 x 7 = 98
14 x 8 = 112
14 x 9 = 126
14 x 10 = 140
#print characters of a string
name="Drashti"
for letter in name:
    print(letter)

    
D
r
a
s
h
t
i
#sum of numbers from 1 to 5
total=0
>>> for i in range(1,6):
...     total=total+i
...     print("sum is:",total)
... 
...     
sum is: 1
sum is: 3
sum is: 6
sum is: 10
sum is: 15
>>> #print list elements
>>> numbers=[10,20,30,40]
>>> for n in numbers:
...     print(n)
... 
...     
10
20
30
40
