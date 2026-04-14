'''
Given two integers X (positive) and N, print the value of X raised to the power of N
'''

def solve(x: int, n: int) -> float:
    '''
    Hypothesis:
        solve(x, n) -> will return the value of x^n
    Induction:
        solve(x, n-1) -> will return the value of x^(n-1)
    Therefore,
        solve(x, n) = 1,                    if n = 0
                    = solve(x, n-1),        if n > 0
                    = 1.0 / solve(x, -n),   if n < 0
    '''
    if n == 0:
        return 1.0
    if n > 0:
        return x * solve(x, n-1)
    return 1.0 / solve(x, -n)
    
x = int(input('Enter the base: '))
n = int(input('Enter the exponent: '))
ans = solve(x, n)
print(ans)