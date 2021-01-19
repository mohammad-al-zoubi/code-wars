from itertools import chain, repeat


def find(a):
    if a <= 3:
        return [0, 1, 2, 2][a]
    arr = [[2]]
    arr_sum = 5
    arr_len = 4
    for i, arr_i in enumerate(chain.from_iterable(arr), 3):
        arr_sum += i * arr_i
        if arr_sum >= a:
            r = (arr_sum - a) // i
            print('r: ', r)
            print('arr_sum: ', arr_sum)
            return arr_len + arr_i - (r + 1)
        arr.append(repeat(i, arr_i))
        arr_len += arr_i
