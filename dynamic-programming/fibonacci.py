def fibonacci(n):
    memo = [0] * n
    memo[0:2] = [0, 1]

    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[0:n]

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))