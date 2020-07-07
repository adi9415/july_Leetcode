# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length  = len(digits)
        num = 0
        for i in digits:
            num += i * (10**(length-1))
            length -= 1
        # print("num",num)  
        num1 = num+1
        
        li = []
        
        while(num1>0):
            r = num1%10
            li.append(r)
            num1 = num1/10
        # print("li",li)    
        return reversed(li)
            