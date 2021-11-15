class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        augend = {}
        for i, n in enumerate(nums):
            augend[target-n] = i
        
        for i, n in enumerate(nums):
            if n in augend and i != augend[n] :
                return [i, augend[n]]

# Time Complexity
# - 2 for loops, each action in code block is O(1)
# Therefore total is 2 * n * O(1) = O(n)

# Space Complexity
# - nums: O(n)
# - augend: n key-value pair, thus O(n)
# Therefore O(n) + O(n) = O(n)

# Results
# 52 / 52 test cases passed.
# Status: Accepted
# Runtime: 52 ms, faster than 97.18% of Python3 online submissions for Two Sum.
# Memory Usage: 15.6 MB, less than 13.03% of Python3 online submissions for Two Sum.
