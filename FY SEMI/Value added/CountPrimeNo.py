
def countPrimes(n):
    count = 0

    for i in range(2, n):
        root = int(i ** 0.5)
        prime = True

        for j in range(2, root + 1):
            if i % j == 0:
                prime = False
                break

        if prime:
            count += 1

    return count

n = int(input("Enter a number: "))
print(countPrimes(n))
