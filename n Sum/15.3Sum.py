class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        account = defaultdict(int)
        nums2 = []
        for n in nums:
            if account[n] < (2 if n else 3):
                account[n] += 1
                nums2.append(n)

        del account
        del nums

        target = defaultdict(list)
        for i, n in enumerate(nums2):
            target[-n].append(i)

        answers = []
        duplicate = set()
        for ia in range(len(nums2)):
            for ib in range(ia+1, len(nums2)):
                # -note 1- s = nums2[ia] + nums2[ib]
                # -note 1- if s in target:
                if nums2[ia] + nums2[ib] in target:
                    for ic in target[nums2[ia] + nums2[ib]]:
                        if ia != ic != ib:
                            # -note 1- ans = [nums2[ia], nums2[ib], -s]
                            ans = [nums2[ia], nums2[ib], nums2[ic]]
                            ans.sort()
                            if tuple(ans) not in duplicate:
                                answers.append(ans)
                                duplicate.add(tuple(ans))
                                break


# Time Complexity
# - 2 1-layer for loops, each action in code block is O(1)
# - 1 2-layer for loop, there are total n^2 / 2 * 2 actions max
#   (* 2) since this is 3Sum, same number (exclude 0) appears at most 2 times
# Therefore total is 2 * n * O(1) + O(n^2) = O(n^2)

# Space Complexity
# if there are m unique numbers, a answer (hard to know)
# - nums: O(n)
# - account: m key-value pair, thus O(m)
# - nums2: O(m)
# - target: m key-value pair, thus O(m)
# - answers: O(a)
# - duplicate: O(a)
# Therefore O(n) + 3O(m) + 2O(a)

# Results
# 52 / 52 test cases passed.
# Status: Accepted
# Runtime: 660 ms, faster than 95.46% of Python3 online submissions for 3Sum.
# Memory Usage: 18.8 MB, less than 9.34% of Python3 online submissions for 3Sum.
# - note 1- improve time complexity from 712 ms to 660 ms
