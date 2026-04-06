Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
n=int(input("enter number of lines: "))
enter number of lines: 4
for i in range (1,n+1):
    print("*"*i)

    
*
**
***
****
for i in range(1,5):
    print("*"*i)

    
*
**
***
****

n=5
for i in range(1,n+1):
    print(j,end="")
    print()

    
Traceback (most recent call last):
  File "<pyshell#12>", line 2, in <module>
    print(j,end="")
NameError: name 'j' is not defined
n=5
for i in range(1,n+1):
    print(j,end="")
print()
SyntaxError: invalid syntax
 n=5
 
SyntaxError: unexpected indent
n=5
for i in range(1,n+1):
    print(j,end="")
    print()

    
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    print(j,end="")
NameError: name 'j' is not defined
n=5
for i in range(1,n+1):
    print(i,end="")
    print()

    
1
2
3
4
5
n=5
for i in range(1,j+1):
    print(j,end="")
    print()

    
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    for i in range(1,j+1):
NameError: name 'j' is not defined
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

    
1
12
123
1234
12345

n=int(input("enter number of lines:"))
enter number of lines:4
i=1
while i<=n:
...     print("*"*i)
...     i+=1
... 
...     
*
**
***
****
>>> n=int(input("enter number of lines: "))
enter number of lines: 4
>>> i=n
>>> while i>=1:
...     print("*"*i)
...     i-=1
... 
...     
****
***
**
*
