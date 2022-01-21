def collatz (n):
    if n <= 0:
        return
    elif n % 2 == 0:
        print(n//2)
        return n //2
    elif n % 2 == 1:
        x = 3 * n + 1
        print(x)
        return x

n = input()
count = 0
while n != 1:
    count += 1
    n = collatz(int(n))
print("times:")
print(count)