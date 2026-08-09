class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # at each choice, want to maximize alice - bob/bob - alice
        # instead of recursive + memo, can do dp since just indexing 1 array
        # time complexity: O(n * 3) = O(n)
        # space complexity: O(n)
        n = len(stoneValue)
        dp = [0] * (n + 1)
        # for dp, to simulate recursive stack propogating back up, work backwards
        # since need 'future value' to get original value
        for i in range(n - 1, -1, -1):
            total = 0
            dp[i] = float('-inf')
            # loop for each choice (1,2,3 rocks)
            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                dp[i] = max(dp[i], total - dp[j + 1])
        # dp[0] is the score of alice minus bob
        score = dp[0]
        if score > 0:
            return "Alice"
        if score < 0:
            return "Bob"
        return "Tie"