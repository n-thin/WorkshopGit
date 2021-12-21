def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def mult(x,y):
  return x*y
def div(x,y):
  return x/y

n1=float(input("Enter the first operand : "))
op=input("Enter the operator [+,-,*,/] : ")
n2=float(input("Enter the second operand : "))

if op=='+':
  print(n1,op,n2,'=',sum(n1,n2))
elif op=='-':
  print(n1,op,n2,'=',sub(n1,n2))
elif op=='*':
  print(n1,op,n2,'=',mult(n1,n2))
elif op=='/':
  print(n1,op,n2,'=',div(n1,n2))
else:
  print("Invalid input!!!")
