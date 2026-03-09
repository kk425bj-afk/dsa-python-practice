# This function calculates the sum of the digits of a given integer m.

def sum_of_digit(m):
  total = 0
  n = abs(m)
  while n > 0:
    total += n % 10
    n //= 10
  return total

# Test cases
print(sum_of_digit(123))  # Output: 6
print(sum_of_digit(-456)) # Output: 15