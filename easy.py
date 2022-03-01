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
#Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        swap first string w/ last string, 2nd element w/ 2nd to last, etc.
        find middle element to stop swapping/split list in half to swap
        """
        
        swap = len(s) // 2
        
        for i in range(swap):
            current_number = s[i]
            current_neg_number = s[(i+1) * -1]
            s[i] = current_neg_number
            s[(i+1) * -1] = current_number

##########################################################################################