def damerau_levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    da = {ch: i for i, ch in enumerate(s1)}
    for i in range(1, m + 1):
        db = 0
        for j in range(1, n + 1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            if s1[i-1] == s2[j-2] and s2[j-1] == s1[i-2]:  # Transposition
                db = max(db, j - 2)
                dp[i][j] = min(dp[i][j], dp[i-2][db] + cost + 1)
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)
    return dp[m][n]