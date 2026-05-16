#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
# list.insert(position, number) - добавляет на указанную позицию

"""
# Моя попытка не самой лучшей реализации
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if (len(nums2) < 1):
            return None
        index2 = 0
        for i in range(len(nums1)):
            if nums1[i] <= nums2[index2] and nums1[i] != 0:
                continue
            t = nums2[index2]
            index2 = (index2 + 1) % n
            for j in range(i, len(nums1)):
                t2 = nums1[j]
                nums1[j] = t
                t = t2
                if t == 0:
                    break

"""
"""
#Вариант настолько простой что я о нём не подумал
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
"""

#более хитрый вариант
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1



solution = Solution()
nums1 = [2,0]
nums2 = [1]
m=1
n=1
solution.merge(nums1,m,nums2,n)
print(nums1)
