Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #basic slices
>>> from array import array
>>> arr=array('i',[10,20,30,40,50])
>>> print(arr[1:4])
array('i', [20, 30, 40])
>>> print(arr[:3])
array('i', [10, 20, 30])
>>> print(arr[2:])
array('i', [30, 40, 50])
>>> print(arr[:])
array('i', [10, 20, 30, 40, 50])
>>> 
>>> #slicing with step
>>> arr=array('i',[10,20,30,40,50,60,70,80])
>>> print(arr[::2])
array('i', [10, 30, 50, 70])
>>> print(arr[1::2])
array('i', [20, 40, 60, 80])
>>> print(arr[::3])
array('i', [10, 40, 70])
>>> 
>>> #negative slcing
>>> arr=array('i',[10,20,30,40,50])
>>> print
<built-in function print>
>>> 
(
>>> print(arr[-4:-1])
array('i', [20, 30, 40])
>>> print(arr[-3])
30
>>> print(arr[-3:])
array('i', [30, 40, 50])
>>> print(arr[:-2])
array('i', [10, 20, 30])
>>> 
>>> #reverse array using slicing
>>> arr= array('i',[10,20,30,40,50])
>>> print(arr[::-1])
array('i', [50, 40, 30, 20, 10])
>>> 
>>> #modifying slices
>>> arr=array('i',[10,20,30,40,50])
>>> arr=[1:4]=array('i',[25,35,45])
SyntaxError: invalid syntax
>>> arr[1:4]=array('i',[25,35,45])
>>> print(arr)
array('i', [10, 25, 35, 45, 50])
>>> 