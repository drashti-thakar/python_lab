try:
     number1= int(input("enter a number: "))
     number2= int(input("enter another number: "))
     result= number1 / number2
except zerodivisionerror:
    print("you cannot divide by zero")
except valueerror:
    print("please enter a valid number")
else: 
    print("division sucessfull result is:",result)
finally: 
    print("this block always runs")