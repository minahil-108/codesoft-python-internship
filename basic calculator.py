#BASIC CALCULATOR
print("\n\t\t\tBASIC CALCULATOR")
x=input("\ndo you want to do some calculations:(y/n)?")
while x=="y":
  num1=int(input("\nplease enter 1 number:"))
  num2=int(input("\nplease enter 2 number:"))
  num=0

  choice=input("\nyou have following operation choices, please select any:\nadd\nsub\nmul\ndiv\n")
  if choice=="add":
    num=num1+num2
    print(f"\naddition={num}")
  elif choice=="sub":
    num=num1-num2
    print(f"\nsubstraction={num}")
  
  elif choice=="mul":
    num=num1*num2
    print(f"\nmultiplication={num}")
  elif choice=="div":
    num=num1/num2
    print(f"\ndivision={num}")

  else:
    print("\ninvalid choice :(")
  
  x=input("\ndo you want to do some calculations:(y/n)?")
    
