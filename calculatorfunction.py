def add(num1,num2):
    return(num1+num2)
def substract(num1,num2):
    return(num1-num2)
def multiply(num1,num2):
    return(num1*num2)
def divide(num1,num2):
    return(num1/num2)




while True:
    choice=input("enter your choice (1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1=float(input("enter first num:"))
        num2=float(input("enter second num:"))
        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print(num1,'-',num2,'=',substract(num1,num2))
        elif choice == '3':
            print(num1,'*',num2,'=',multiply(num1,num2))
        elif choice =='4':
            print(num1,'/',num2,'=',divide(num1,num2))
        next_calculation = input("let do next calculation(yes/no):")
        if next_calculation == "no":
            break
    else:
        print("invalid input")