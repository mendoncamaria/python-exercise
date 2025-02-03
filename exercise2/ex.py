from os import *
from sys import *
from collections import *
from math import *

def optimalStrategyOfGame(coins, n):
    # Write your function here.
    n = len(coins)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = coins[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(
                coins[i] + min(dp[i + 1][j - 1], dp[i + 2][j] if i+2<=j else 0),
                coins[j] + min(dp[i + 1][j - 1], dp[i][j - 2] if j-2>=i else 0)
            )

    return dp[0][n - 1]
