choice=input("Enter your choice: sum, dif, mul, div")
def sum ():
  num1= int(input("Enter your first number: "))
  num2=int(input("Enter your second number: "))
  total=num1+num2
  print("The sum is", total)
def dif ():
    num1= int(input("Enter your first number: "))
    num2=int(input("Enter your second number: "))
    total=num1-num2
    print ("The difference is", total)
def mul ():
    num1= int(input("Enter your first number: "))
    num2=int(input("Enter your second number: "))
    total=num1*num2
    print ("The product is", total)
def div ():
   num1= int(input("Enter your first numberL "))
   num2=int(input("Enter your second number: "))
   total=num1/num2
   print ("The dividend is", total)


if choice == "sum" :
   sum()
elif choice == "dif" :
   dif()
elif choice == "mul":
   mul()
elif choice == "div" :
   div()
else :
   print("Invalid Input!")