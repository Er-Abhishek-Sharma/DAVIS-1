"""Write a programe to input the no. is all factors"""

def all_factors(n):
  
  factors = []
  
  for i in range(1, n+1):
    if n % i == 0:
      factors.append(i)
      return factors
    
number = int(input(""))
print(all_factors(number))