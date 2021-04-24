class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        
        memory = [None] * (right + 1)
        return self.sumFromZero(right, memory) - self.sumFromZero(left-1, memory)
        
        
    def sumFromZero(self, target, memory):
        if target == -1:
            return 0
        
        if memory[target] != None:
            return memory[target]
        
        output = self.nums[target] + self.sumFromZero(target-1, memory)
        memory[target] =  output
        return output
        
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
