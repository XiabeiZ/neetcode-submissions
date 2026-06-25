class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or nums == None:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[(left + right) // 2] == target:
                return (left + right) // 2
            elif nums[(left + right) // 2] > target:
                right = (left + right) // 2 - 1
            else:
                left = (left + right) // 2 + 1
        return -1