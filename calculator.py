print("    CALCULATOR    ")

num1=float(input("Enter a first number:"))
num2=float(input("Enter a second number:"))

print("1.'+'\n2.'-'\n3.'*'\n4.'/'\n5.'%'")

choise = int(input("enter your choice form 1-5:"))

if choise ==1:
    print(f"{num1} + {num2} =",num1+num2)
elif choise ==2:
    print(f"{num1} - {num2} =",num1-num2)
elif choise ==3:
    print(f"{num1} * {num2} =",num1*num2)
elif choise ==4:
    print(f"{num1} / {num2} =",num1/num2)
elif choise ==5:
    print(f"{num1} % {num2} =",num1%num2)
else :
    print(" invalid input")