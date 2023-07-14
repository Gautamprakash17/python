from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

nums = [2, 7, 10, 15, 45, 2, 6, 3, 5, 10, 12, 10, 4, 9]
target = 9
result = Solution.twoSum(nums, target)
print("Indexes are:", result)
