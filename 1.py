import math
import functools
m=int(input("m ="))
while(m<4):
    m=int(input("m ="))
z=math.sqrt((m+3)/(m-3))
print("z=  √((m+3)/(m-3))")
print("z=",z)
n=int(input("n="))
if(n<3):
     print("білше")
while(n<3):
    n=int(input("n="))
    if(n<3):
     print("білше") 
y=1
for i in range(0,n*2,2):
    i+=2
    y=y*i
print("y=",y)



