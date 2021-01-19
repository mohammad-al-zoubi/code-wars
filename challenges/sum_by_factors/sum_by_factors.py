def prime_factors(n):
    """
    Calculates the prime factors of an integer
    :param n: Integer
    :return: factors <array>
    """
    n = abs(n)
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


def get_prime_numbers(arr):
    """
    Returns the needed prime numbers for calculating the array
    :param arr: list of integers
    :return: prime numbers between 0 and the largest element in arr
    """
    n = max((max(arr), abs(min(arr)))) + 1
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


def sum_for_list(lst):
    p_nums = get_prime_numbers(lst)
    result = []
    for p in p_nums:
        sum_ = 0
        used = False
        for i in lst:
            if p in prime_factors(i):
                used = True
                sum_ += i
        if used:
            result.append([p, sum_])
    return result
