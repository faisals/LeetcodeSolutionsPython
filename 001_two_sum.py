
nums = [2,7,11,15]
target = 9
arr=[]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        for i,n in enumerate(nums):
            if (target-n) in nums[:i] + nums[i+1:]:
                arr.append(i)
        
        return arr 
