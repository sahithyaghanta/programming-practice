a=int(input("enter first number:"))
b=int(input("enter second number:"))

print("1.addition=",a+b)
print("2.subtraction=",a-b)
print("3.multiplication=",a*b)
print("4.division=",a//b)
print("5.modulus=",a%b)
choice=int(input("enter your choice:"))

if choice==1:
  print("result=",a+b)
elif choice==2:
  print("result=",a-b)
elif choice==3:
  print("result=",a*b)
elif choice==4:
  print("result=",a//b)
elif choice==5:
  print("result=",a%b)
else:
  print("invalid choice")
