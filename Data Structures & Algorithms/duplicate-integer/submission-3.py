class Solution:
    def hasDuplicate(self, nums: List) -> boolean:
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False