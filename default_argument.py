def greet(name,msg="good morning"):
   print("hello",name+",",msg)
greet("drashti")
greet("raj","good evening")
def power(num,exp=2):
    return num**exp
print(power(3))
print(power(3,3))
print(power(2,4))
def student_info(name,age=18,course="abc"):
    print("name:",name)
    print("age:",age)
    print("course:",course)
student_info("raj")
student_info("drashti",19)
student_info("radhu",20,"bscIT")