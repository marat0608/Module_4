from math import inf

def true_divide(first, second):
    if second == 0:
        print('inf')
    else:
        print(first / second)

result3 = true_divide(49, 7)
result4 = true_divide(15, 0)