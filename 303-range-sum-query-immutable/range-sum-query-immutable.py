class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.total = 0
        

    def sumRange(self, left: int, right: int) -> int:
        self.total = 0
        while left <= right:
            self.total += self.nums[left]
            left += 1
        
        return self.total
        



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)