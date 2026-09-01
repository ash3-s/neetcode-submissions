class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            nextDP = defaultdict(int)
            for curSum, count in dp.items():
                nextDP[curSum + nums[i]] += count
                nextDP[curSum - nums[i]] += count
            dp = nextDP
        return dp[target]