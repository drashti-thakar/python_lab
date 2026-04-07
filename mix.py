Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
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
for i in range(1,21):
    if i%2==0:
        print()

        










for i in range(1,21):
    if i%2==0:
        print(i)

        
2
4
6
8
10
12
14
16
18
20
print i in range(1,16):
    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
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
for i in range(1,11):
    print("5x",i,"=",5*i)

    
5x 1 = 5
5x 2 = 10
5x 3 = 15
5x 4 = 20
5x 5 = 25
5x 6 = 30
5x 7 = 35
5x 8 = 40
5x 9 = 45
5x 10 = 50
i=1
while i<10:
    print(i)
    i=i+1

    
1
2
3
4
5
6
7
8
9
n=int(input("enter n:"))
enter n:4
i=1
s=0
while i<=n:
    s=s+i
    i=i+1
    print("sum= ",s)

    
sum=  1
sum=  3
sum=  6
sum=  10
num=int(input("enter number: "))
enter number: 14
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1

    
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
>>> #udf check even or odd
>>> def even(num):'
SyntaxError: unterminated string literal (detected at line 1)
>>> def even(num):
...     if num%2==0:
...         return True
...     else:
...         return False
...     print(even(14))
...     print(even(7))
... 
...     
