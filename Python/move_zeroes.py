'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #Overview:
        #we are splitting the list into zero and non-zero values, then merging the list afterwards
        
        #count of how many zeroes are in the list
        zero_count = 0
        
        #empty list to hold zeroes
        zero_list = []
        
        #for each number of List
        for num in nums:
            
            #if the num is zero
            if num == 0:
                
                #add a zero to the list of zeroes
                zero_list.append(num)
                
                #indicate to zero count there was one more zero
                zero_count +=1
                
        #while the zero_count is greater than 0
        while zero_count > 0:
            
            #remove a zero from the original list
            nums.remove(0)
            
            #and reduce the count by 1
            zero_count -=1
                
        #remaining list after zeroes are removed is a list of all non-zero values
        nums = nums.extend(zero_list)