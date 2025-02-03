import requests
def isArmStrong(num: int):
    num_str = str(num)
    if num_str.startswith("-"):
        my_num = num_str[1:]
    else:
        my_num = num_str
    num_len = len(my_num)
    armstrong_sum = sum([int(digit) ** num_len for digit in my_num])

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
      if digit == '-' :
          continue
      sum += int(digit)       
    return sum
def get_fun_fact(num): 
    headers = {'Accept': 'application/json'}
    response = requests.get(f'http://numbersapi.com/{num}/math',headers=headers)
    fun_fact = response._content 
    return fun_fact

def is_perfect(n):
    if str(n).startswith('-'):
        return False
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
    if str(num).startswith('-'):
        return False
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