'''
Given a positive integer N, print the numbers from 1 to N
'''

def solve(n: int) -> None:
    '''
    Expectation:
        solve(n) -> will print numbers from 1 to n
    Faith:
        solve(n-1) -> will print numbers from 1 to n-1
    Therefore,
        solve(n) = solve(n-1) + print(n)
    '''

    if n < 1:
        return

    solve(n-1)
    print(n)

solve(int(input('Enter a positive integer: ')))