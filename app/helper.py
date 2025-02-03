
def isArmStrong(num: int):
    num_str = str(num)
    num_len = len(num_str)
    armstrong_sum = sum([int(digit) ** num_len for digit in num_str])

    if armstrong_sum == num:
        return True
    else:
        return False
    
def is_even(num:int):
    if (int(num) % 2) == 0:
        return True
    else:
        return False 
    

def getSum(n): 
   
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum

def is_perfect(n):
    # Initialize a variable 'sum' to store the sum of factors of 'n'
    sum = 0
    
    # Iterate through numbers from 1 to 'n-1' using 'x' as the iterator
    for x in range(1, n):
        # Check if 'x' is a factor of 'n' (divides 'n' without remainder)
        if n % x == 0:
            # If 'x' is a factor of 'n', add it to the 'sum'
            sum += x
    
    # Check if the 'sum' of factors is equal to the original number 'n'
    return sum == n


def is_prime(num: int):  
    if num > 1:
  
    # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
      
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return  False
        else:
            return True
    else:
        return False