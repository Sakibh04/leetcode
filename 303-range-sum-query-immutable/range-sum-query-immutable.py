class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        for i in range (len(self.nums)):
            if i == 0:
                self.nums[i] = self.nums[i]
            else:
                self.nums[i] = self.nums[i-1] + self.nums[i]

        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            res = self.nums[right] - self.nums[left-1]
        else:
            res = self.nums[right]
        return res
        



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)