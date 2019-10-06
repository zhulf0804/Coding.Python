from typing import List
from random import randrange
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.originals = list(nums)
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.originals

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums)):
            swap_ind = randrange(i, len(self.nums))
            self.nums[i], self.nums[swap_ind] = self.nums[swap_ind], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()