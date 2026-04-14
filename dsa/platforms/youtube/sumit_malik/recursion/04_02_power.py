'''
Given two integers X and N, print the value of X raised to the power of N
Note: Optimized solution with O(log N) time complexity
'''

def solve(x: int, n: int) -> float:
    '''
    Hypothesis:
        solve(x, n) -> will return the value of x^n
    Induction:
        solve(x, n-1) -> will return the value of x^(n-1)
    Therefore,
        solve(x, n) = x * solve(x, n-1),    if n > 0
                    = solve(x, n+1) / x,    if n < 0
                    = 1,                    if n == 0
                    = 0,                    if x == 0 and n > 0
                    = undefined,            if x == 0 and n <= 0

    '''
    if x == 0 and n == 0:
        raise ValueError('0 raised to the power of 0 is undefined')
    if x == 0 and n < 0:
        raise ZeroDivisionError('0 cannot be raised to a negative power')
    if x == 0:
        return 0.0
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / solve(x, -n)
    half_power = solve(x, n >> 1)
    return x * half_power * half_power if n & 1 else half_power * half_power


x = int(input('Enter the base: '))
n = int(input('Enter the exponent: '))
ans = solve(x, n)
print(ans)