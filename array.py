Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #len()-number of element
>>> from array import array
>>> arr=array('i', [10,20,30,40,50])
>>> print(len(arr))
5
>>> 
>>> #append(X)- add element at end
>>> arr=array('i',[10,20,30])
>>> arr.append(40)
>>> print(arr)
array('i', [10, 20, 30, 40])
>>> 
>>> #insert(pos,x)Insert at position
>>> arr=array('i',[10,20,40])
>>> arr insert(2,30)
SyntaxError: invalid syntax
>>> arr=array('i',[10,20,40])
>>> arr.insert(2,30)
>>> print(arr)
array('i', [10, 20, 30, 40])
>>> 
>>> #remove(x)- Remove first occurrence
\
>>> arr=array('i',[10,20,30,20,40])
>>> arr.remove(20)
>>> print(arr)
array('i', [10, 30, 20, 40])
>>> 
>>> #pop- remove and return last element
>>> arr=array('i',[10,20,30,40])
>>> x=arr.pop()
>>> print("removed:",x)
removed: 40
>>> print(arr)
array('i', [10, 20, 30])
>>> 
>>> #index(x) - find index of element
>>> arr=array('i',[10,20,30,40])
>>> print(arr.index(30))
2
>>> #count(X)-count occurrences
>>> arr=array('i',[10,20,30,20,40])
>>> print(arr.index(30))
2
>>> 
>>> #reverse()-reverse array
>>> arr= array('i',(10,20,30,40))
>>> arr.reverse()
>>> print(arr)
array('i', [40, 30, 20, 10])
>>> 