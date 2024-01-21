#Write a python code to find given number is prime or not

'''
#v1
def main():
  n = int(input("Enter a number: "))
  isPrime(n)
  
def isPrime(n):
  if n <= 1:
    print(f"{n} isn't a prime number.")
    
  for i in range(2, n//2):
    if n % i == 0:
      print(f"{n} isn't a prime number.")
      break
      
  else:
      print(f"{n} is a prime number.")
  
main()
'''
#v2
def main():
  n = int(input("Enter a number: "))

  if isPrime(n):
    print(f"{n} is a prime number.")
  else:
    print(f"{n} isn't a prime number.")
  
def isPrime(n):
  if n <= 1:
    return False
    
  for i in range(2, n//2):
    if n % i == 0:
      return False    
  else:
    return True
  
main()