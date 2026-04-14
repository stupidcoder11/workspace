'''
Given two positive integers X and N, print the value of X raised to the power of N
'''

def solve(x: int, n: int) -> float:
    '''
    Hypothesis:
        solve(x, n) -> will return the value of x^n
    Induction:
        solve(x, n-1) -> will return the value of x^(n-1)
    Therefore,
        solve(x, n) = x * solve(x, n-1),    if n > 0
                    = 1,                    if n == 0
    '''
    if n == 0:
        return 1.0
    return x * solve(x, n-1)

x = int(input('Enter the base: '))
n = int(input('Enter the exponent: '))
ans = solve(x, n)
print(ans)