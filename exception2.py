try:
    my_list=[1,2,3]
    print(my_list[1])
except indexerror:
    print("index is out of range!")
else:
    print("element found successfully!")
finally:
    print("program finished.")