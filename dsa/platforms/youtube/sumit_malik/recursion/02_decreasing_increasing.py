'''
Given a positive integer N, print the numbers from N to 1
'''

def solve(n: int) -> None:
    '''
    Expectation:
        solve(n) -> will print numbers from n to 1
    Faith:
        solve(n-1) -> will print numbers from n-1 to 1
    Therefore,
        solve(n) = print(n) + solve(n-1)
    '''

    if n < 1:
        return

    print(n)
    solve(n-1)

solve(int(input('Enter a positive integer: ')))