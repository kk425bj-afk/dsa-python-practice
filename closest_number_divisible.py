# This function finds the closest number to n that is divisible by m.

def closest_num(n, m):
  lower = (n // m) * m
  upper = lower + m
  if abs(n - lower) < abs(n - upper):
    return lower
  elif abs(n - lower) > abs(n - upper):
    return upper
  else:
    if abs(lower) > abs(upper):
      return lower
    else:
      return upper

# Test cases
print(closest_num(10, 3))  # Output: 9
print(closest_num(14, 5))  # Output: 15