Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #positive indexing
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> print(arr[0])
10
>>> print(arr[2])
30
>>> print(arr[4])
50
>>> #negative indexing
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> print(arr[-1])
50
>>> print(arr[-2])
40
>>> print(arr[-5])
10
>>> #modifying elements using index
>>> arr=array('i',[10,20,30,40,50])
>>> arr[2]=35
>>> print(arr)
array('i', [10, 20, 35, 40, 50])
>>> 