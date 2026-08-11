class Solution(object):
    def missingInteger(self, nums):
        sequentialSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                sequentialSum += nums[i]
            else:
                break
        hashTable = [False] * 1276
        for num in nums:
            hashTable[num] = True
        while hashTable[sequentialSum]:
            sequentialSum += 1

        return sequentialSum

