class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        prefix = 1
        res = []
        for i in nums:
            res.append(prefix)
            prefix *= i
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *=  postfix           
            postfix *= nums[i]
        return res