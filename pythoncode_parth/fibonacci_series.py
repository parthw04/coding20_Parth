def fibonacci(n):
    fseries = [0, 1]
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return [0]
    elif n == 2:
        return fseries
    else:
        while len(fseries) < n:
            fseries.append(fseries[-1] + fseries[-2])
        return fseries


n = int(input("Enter the number of terms: "))
fseries = fibonacci(n)
print("Fibonacci series up to the", n, "th term:", fseries)
