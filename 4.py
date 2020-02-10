# Euler Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


pal_nums = []

def reverse(num): 
  str = "" 
  for i in num:
    str = i + str
  return str

for i in range(100,999):
    for x in range(100,999):
        num = (str)(i * x)
        if num == reverse(num):
            pal_nums.append((int)(num))

print(max(pal_nums))
