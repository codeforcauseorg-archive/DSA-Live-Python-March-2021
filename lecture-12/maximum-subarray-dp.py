# https://leetcode.com/problems/range-sum-query-immutable


class NumArray:

    def __init__(self, nums: List[int]):

        
        for idx in range(1, len(nums)):
            nums[idx]  = nums[idx] + nums[idx-1]
                
        self.prefixSum = nums
        
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.getPrefixSum(right) - self.getPrefixSum(left-1) 
    
    def getPrefixSum(self, target: int) -> int:
        
        if target == -1:
            return 0
        
        return self.prefixSum[target]
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
