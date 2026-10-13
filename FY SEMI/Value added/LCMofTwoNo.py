
def findLcm(n1, n2):
    a = n1
    b = n2

    while b != 0:
        a, b = b, a % b

    gcd = a
    lcm = (n1 * n2) // gcd

    return lcm


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(findLcm(n1, n2))