print("Press to  a and b")
x=int
a=int(input("a ="))
while( a < 1 ):
 a=int(input("a ="))
b=int(input("b ="))
while(b < 1):
  b=int(input("b ="))
if a>b:
 x= 5*a+b
 print(" x= 2*a+b")
 print(" x=",x)
 
elif a==b:
    x =-125
    print("x=",x)
elif a <b:
    x=(a-5)/b
    print("x=",x)




