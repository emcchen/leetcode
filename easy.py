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
#Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        string_reversed = string[::-1]
        
        if x < 0:
            return False
        else:
            if string == string_reversed:
                return True

##########################################################################################
#Binary Search on practice.geeksforgeeks.org
#Check if we looked through all numbers in array.. If so return -1

class Solution:
    def binarysearch(self, arr, n, k):
        low = 0
        high = n - 1
        mid = 0

        while low <= high:
            middle = (low + high) // 2
            
            if arr[middle] < k:
                low = middle + 1
            elif arr[middle] > k:
                high = middle - 1
            else:
                return middle
        return -1
    
    # Time complexity log(n)
    # Space complexity O(1)

##########################################################################################
#Valid Parenthesis
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {'(':')', '{':'}', '[':']'}
        
        for character in s:
            if character in brackets:
                stack.append(brackets[character])
            elif stack and stack[-1] == character:
                stack.pop()
            else:
                return False
        return len(stack) == 0

##########################################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#loop until there is no more linkedlist
#identify the head as the current node
#Set previous node as None
#set variable as current's next and reverse it
#update previous and current

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        previous = None
        
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

    Time complexity O(n), Space complexity O(1)

##########################################################################################