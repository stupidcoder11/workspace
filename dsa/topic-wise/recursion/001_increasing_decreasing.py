n: int = 5

'''
Given -
n, an integer

Expectation -
Print the numbers from n to 1 in decreasing order and then from 1 to n in increasing order.
For example, if n = 3, the output should be:
3
2
1
1
2
3
'''

def increasing_decreasing(n: int) -> None:
    '''
    Assuming this function will print numbers from n to 1 in decreasing order 
    and then from 1 to n in increasing order.
    '''
    if n < 1:
        return
    print(n)
    increasing_decreasing(n - 1)
    print(n)

if __name__ == "__main__":
    increasing_decreasing(n)