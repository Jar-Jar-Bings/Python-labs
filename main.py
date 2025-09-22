from mod1 import product
n=int(input("n="))

if(n<=1):
    print("білше")
    
while(n<=1):
    n=int(input("n="))
    
    if(n<=1):
     print("білше")
     
print("y =", product(n))
