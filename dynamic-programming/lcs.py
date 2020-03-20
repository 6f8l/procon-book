def lcs(a, b):
    x, y = len(a), len(b)
    dp = [[0] * (y + 1) for _ in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if dp[i - 1] == dp[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[x][y]

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a = input()
        b = input()
        print('===========')
        print(lcs(a, b))