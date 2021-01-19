from itertools import permutations


def next_bigger(num):
    num_str = str(num)
    bigger_nums = []
    if all(num_str[i] == num_str[(i+1)%len(num_str)]
           for i in range(len(num_str))) or len(num_str)==1:
        return -1

    for comb in permutations(range(len(num_str)), r=len(num_str)):
        num_comb = (''+ num_str[x] for x in comb)
        num_comb = int(''.join(num_comb))
        if num_comb > num:
            bigger_nums.append(num_comb)
        if comb[0] > 1:
            break
    bigger_nums.sort()
    # print(bigger_nums)
    if bigger_nums:
        return bigger_nums[0]
    else:
        return -1
