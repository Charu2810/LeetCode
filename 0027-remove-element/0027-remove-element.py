class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in range(len(nums)):
            result=[]
            if nums[i] !=val:
                result.append(nums[i])
                nums[count]=nums[i]
                count+=1
        return count
        