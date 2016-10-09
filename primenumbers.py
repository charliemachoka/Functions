def primenumbers(n):
   for num in range(2,n+1):
      if all(num % i != 0 for i in range(2,num)):
         print (num)

print(primenumbers(10))
