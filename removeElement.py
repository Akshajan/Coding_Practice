class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else: 
                i+=1
            
        return nums.length,nums

            
        
def test_remove_element():
    sol = Solution()
    
    # Test Case 1: Simple removal
    nums = [3, 2, 2, 3]
    val = 3
    length, result = sol.removeElement(nums[:], val)
    print(f"Input: [3, 2, 2, 3], val=3 -> Output: Length={length}, List={result}")
    
    # Test Case 2: No element to remove
    nums = [1, 2, 4, 5]
    val = 3
    length, result = sol.removeElement(nums[:], val)
    print(f"Input: [1, 2, 4, 5], val=3 -> Output: Length={length}, List={result}")

    # Test Case 3: All elements removed
    nums = [7, 7, 7]
    val = 7
    length, result = sol.removeElement(nums[:], val)
    print(f"Input: [7, 7, 7], val=7 -> Output: Length={length}, List={result}")
    
    # Test Case 4: Mixed values
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    length, result = sol.removeElement(nums[:], val)
    print(f"Input: [0,1,2,2,3,0,4,2], val=2 -> Output: Length={length}, List={result}")

test_remove_element()
