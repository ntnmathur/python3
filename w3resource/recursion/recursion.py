# 1. Write a Python program to calculate the sum of a list of numbers.
def add_all(nums):
    if len(nums) == 1:
        return nums[0]
    final_sum = nums[0] + add_all(nums[1:])
    return final_sum

# print(add_all([1,2,3]))

# 3. Write a Python program of recursion list sum.
def list_sum(list_of_lists):
    total = 0
    for elem in list_of_lists:
        if type(elem) == list:
            total = total + list_sum(elem)
        else:
            total = total + elem
    return total

# print(list_sum([1, 2, [3,4],[5,6]]))

# 4. Write a Python program to get the factorial of a non-negative integer
def factorial(n):
    if n == 1:
        return 1
    fact = n*factorial(n-1)
    return fact

# print(factorial(5))


# 5. Write a Python program to solve the Fibonacci sequence using recursion.
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))

# 6. Write a Python program to get the sum of a non-negative integer.
def sum_digits(num):
    if num == 0:
        return num
    return num%10 + sum_digits(int(num/10))

# print(sum_digits(345))

# 7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_series(n):
    if n < 1:
        return 0
    else:
        return n + sum_series(n-2)
# print(sum_series(6))
# print(sum_series(10))

# 8. Write a Python program to calculate the harmonic sum of n-1.
def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)

# print(harmonic_sum(7))
# print(harmonic_sum(4))

# 9. Write a Python program to calculate the geometric sum of n-1.
def geometric_sum(n):
    if n < 1:
        return 1
    else:
        return 1/(2**n) + geometric_sum(n-1)
# print(geometric_sum(7))
# print(geometric_sum(4))

# 10. Write a Python program to calculate the value of 'a' to the power 'b'.
def power(a,b):
    if b == 1:
        return a
    else:
        return a*power(a,b-1)
# print(power(3,4))

# 11. Write a Python program to find  the greatest common divisor (gcd) of two integers.
def gcd(a,b):
    low = min(a,b)
    high = max(a,b)

    if low == 0:
        return high
    if low == 1:
        return 1
    else:
        return gcd(low,high%low)

print(gcd(12,14))