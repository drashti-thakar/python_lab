Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="hello world"
print(x);  #str
hello world

x="20"
print(x);   #int
20

x="20.5"
print(x);   #float
20.5

x="1j"
print(x);   #complex
1j

x=["cherry","mango","litchi"]
print(x);     #list
['cherry', 'mango', 'litchi']

x=("cherry","mango","litchi")
print(x);    #tuple
('cherry', 'mango', 'litchi')

x=range(5)
print(x);   #range
range(0, 5)

x={"name":"drashti","age":19}
print(x);    #dict
{'name': 'drashti', 'age': 19}

x={"cherry","mango","litchi"}
print(x);  #set
{'litchi', 'mango', 'cherry'}

x=frozenset({"cherry","mango","litchi"})
print(x);  #bool
frozenset({'litchi', 'mango', 'cherry'})

x=True
print(x); #bool
True

x=b"hello"
print(x);  #bytes
b'hello'

x=bytearray(5)
print(x);  #bytearray
bytearray(b'\x00\x00\x00\x00\x00')

x=memoryview(bytes(5))
print(x);    #memoryview
<memory at 0x0000021AA4393D00>

x=
SyntaxError: invalid syntax
x=none
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x=none
NameError: name 'none' is not defined. Did you mean: 'None'?
