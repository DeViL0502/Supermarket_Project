x=input("Enter the first string: ") 

y=input("Enter the second string: ") 

a=set(x) 

b=set(y) 

c=set() 

while(True): 

    print("Menu:\n1. Intersection\n2.Difference\n3.Union\n4.Symmetric Difference") 

    z=eval(input("Enter your choice: ")) 

 

    if(z==1): 

        c=a&b 

        print(c) 

 

    elif(z==2): 

        c=a-b 

        print(c) 

 

    elif(z==3): 

        c=a|b 

        print(c) 

 

    elif(z==4): 

        c=a^b 

        print(c) 

 

    else: 

        break 
