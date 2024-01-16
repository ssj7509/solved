# 입력을 받습니다.
N, K = map(int, input().split())

# DP 테이블을 초기화합니다. (K+1 x N+1)
dp = [[0] * (N+1) for _ in range(K+1)]

# 0개의 숫자로 0을 만드는 경우의 수는 1입니다.
dp[0][0] = 1

# 다이나믹 프로그래밍 진행 (Bottom-Up 방식)
for i in range(1, K+1):
    for j in range(N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp[i][j] %= 1000000000

# K개의 숫자로 N을 만드는 경우의 수를 출력합니다. (마지막에 더하는 경우와 같으므로 dp[K][N]을 출력)
print(dp[K][N])