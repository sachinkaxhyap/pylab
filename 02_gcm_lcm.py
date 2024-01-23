# Write a python code to find LCM and GCM of a given list

'''import math
def calc_gcd(n1, n2):
  #while n2:
  #    n1, n2 = n2, n1 % n2
  #return n1
  if n2>n1:
    min_num = n1
  else:
    min_num = n2
  
  for i in range(1, min_num+1):
    if n1%i==0 and n2%i==0:
      result = i
    
  return result

def calc_lcm(n1, n2):
  if n1 and n2:
    return (n1 * n2) // calc_gcd(n1, n2)

l = [10, 6]
print(calc_gcd(l[0], l[1]))
print(calc_lcm(l[0], l[1]))
'''
#print(math.lcm(n, m))
#print(math.gcd(n, m))


from math import gcd, lcm

def main():
  numbers_list = [80, 56, 8, 16,]
  GCD = calculate_gcd(numbers_list)
  LCM = calculate_lcm(numbers_list)
  print("GCM: ", GCD)
  print("LCM: ", LCM)

def calculate_gcd(numbers):
  result = numbers[0]
  for number in numbers:
    result = gcd(result, number)
  return result

def calculate_lcm(numbers):
  result = numbers[0]
  for number in numbers:
    result = lcm(result, number)
  return result

if __name__ == '__main__':
  main()
