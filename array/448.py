# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
		n = len(nums)
		nums = set(nums) 
		
		arr = []
		
		for i in range(1, n+1):
			if i not in nums:
				arr.append(i)
		return arr



