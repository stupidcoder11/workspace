x: list[int] = [9]
y: list[int] = [1]

'''
Provided -
1) x, y whole numbers represented as list of digits
2) 0 <= x[i], y[j] <= 9
3) 0 <= len(x), len(y) <= 100

Constraints -
1) No type conversions are allowed

Expectation -
Return the sum of x & y
For e.g. :
1) if x = [1, 2, 3] & y = [1, 2, 4], then x+y = [2, 4, 7]
2) if x = [1, 2] & y = [1], then x+y = [1, 3]
3) if x = [] & y = [2, 1], then x+y = [2, 1]
'''

def x_plus_y(x: list[int], y: list[int]) -> list[int]:
    i = len(x) - 1
    j = len(y) - 1
    carry = 0
    res = []
    while i >= 0 or j >=0 or carry:
        dx = x[i] if i >= 0 else 0
        dy = y[j] if j >= 0 else 0
        dsum = dx + dy + carry
        res.append(dsum % 10)
        carry = dsum // 10
        i, j = i - 1, j - 1
    return res[::-1]

ans = x_plus_y(x, y)
print(ans)
