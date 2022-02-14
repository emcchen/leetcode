#TwoSum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Create dictionary for looking up the paired number
        Loop through list and store in dictionary
        Find paired number... Target - number = pair.
        If pair key is in dictionary, will need to get value of it. Cannot be itself.
        Return the number's value and pair value
        """
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    return x, y
        # Time complexity = O(n^2) Space complexity = O(1)
        
        dictionary = {}
        
        for x in range(len(nums)):
            pair = target - nums[x]
            if pair in dictionary:
                return x, dictionary[pair]
            dictionary[nums[x]] = x
        
        # Time complexity = O(n) Space complexity = O(n)


##########################################################################################