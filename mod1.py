def product(n):
 y=1
 for i in range(0,n*2,2):
     i+=2
     y=y*i
 return y
