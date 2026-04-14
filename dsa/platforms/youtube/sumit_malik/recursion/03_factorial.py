'''
Given a positive integer N, print the factorial of N
'''

def solve(n: int) -> int:
    '''
    Hypothesis:
        solve(n) -> will return the factorial of n
    Induction:
        solve(n-1) -> will return the factorial of n-1
    Therefore,
        solve(n) = n * solve(n-1)
    '''
    if n < 0:
        raise ValueError('Input must be a positive integer')
    if n == 0:
        return 1
    factorial_n_minus_1 = solve(n-1)
    factorial_n = n * factorial_n_minus_1
    return factorial_n

ans = solve(int(input('Enter a positive integer: ')))
print(ans)