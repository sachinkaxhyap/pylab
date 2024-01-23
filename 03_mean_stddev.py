# Write a python code to find mean and standard deviation of a given list of numbers

def main():
  numbers = [10, 12, 23, 23, 16, 23, 21, 16]
  #numbers_input = input("Enter numbers: ").split()
  #numbers = [int(num) for num in numbers_input]
  
  m = mean(numbers)
  sd = stddev(numbers, m)
  print("Mean: ", m)
  print("Standard Deviation: ", sd)

def mean(nums):
  return (sum(nums))/len(nums)

def stddev(nums, mean_):
  x = 0
  for i, num in enumerate(nums):
    x += (num-mean_) **2 / (len(nums)-1) # remove -1 for population and keep -1 fir sample
    
  return x ** 0.5

if __name__ == '__main__':
  main()
  

#stddev formula -->
  #((n1-mean²)+...+(nN-mean²))/(len(numbers) OR count -1)
  # underRoot previous result