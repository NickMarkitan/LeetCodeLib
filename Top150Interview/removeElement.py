"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution(object):
    def removeElement(self, nums, val):
        k = nums.count(val)
        while (nums.count(val) > 0):
            for j in range(len(nums)):
                if (nums[j] == val):
                    nums.pop(j)
                    break




solution = Solution()
nums1 = [3,2,2,3]
m=3
solution.removeElement(nums1, m)
print(nums1)
