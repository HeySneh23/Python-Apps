while True:
    print("1 Addition")
    print("2 Substraction")
    print("3 Mltiplicaition")
    print("4 Division")
    # Complete the rest of the input choices

    choice=input("enter your choice:")
    
    # Complete the input
    num1=float(input("enter number1:"))
    num2=float(input("enter number2:"))

    match choice:
        case "1":
            print(num1,"+",num2, "=",(num1+num2)) 
        case "2":
            print(num1,"-",num2, "=",(num1-num2))
        case "3":
            print(num1,"*",num2, "=",(num1*num2))
        case "4":
            if num2==0.0:
                print("divide by 0 error")
            print(num1,"/",num2, "=",(num1/num2))
        
            

        # Repeat the cases for other choices sub/mul/div

        # use default to break from the loop - Think How
        case default:
            break


