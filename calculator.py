a=int(input("enter your first number  :"))
b=int(input("enter your second number :"))
print("---------simplecalculator----------")
print("1. add (+)")
print("2. subtract (-)")
print("3. multiply (*)")
print("4. divide (/)")
print("5. exit")
choice=input("enter your choice (1/2/3/4/5) :")
if choice == "5":
    print("exit")
    breakpoint
elif choice =='1':
    print("result add",a+b)
elif choice =='2':
    print("result subtract",a-b)
elif choice =='3':
    print("result multiply ",a*b)
elif choice =='4':
    if b !=0:
        print("result",a/b)
    else:
        print("error cannot divide with zero")
else:
    print("soory your entered number invalid")