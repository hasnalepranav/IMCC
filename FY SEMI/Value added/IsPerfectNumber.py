def isPerfectNumber(n):
    sum = 1
    for i in range(2, int(n ** 1/2)):
        if n % i == 0:
            sum += i
            sum += n // i
    return sum == n