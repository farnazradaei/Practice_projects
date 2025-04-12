n = int(input())
if 1 <= n <= 19 and n % 2 != 0:
    for i in range(n):
        if i <= n // 2:
            stars = 2 * i + 1
        else:
            stars = 2 * (n - i - 1) + 1

        spaces = (n - stars) // 2

        print(" " * spaces + "*" * stars + " " * spaces, end="")
        print(" " * spaces + "*" * stars + " " * spaces)