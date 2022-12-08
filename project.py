def is_fib_num(n):
    a = 0
    b = 1
    while b < n:
        c = a + b
        a = b
        b = c
    if b == n or a == n:
        return True
    else:
        return False

nums = [int(i) for i in input("Enter a number or numbers: ").split(',')]

for i in nums:
    if is_fib_num(i):
        print(i, "is a Fibonacci Number")
    else:
        print(i, "is not a Fibonacci Number")
