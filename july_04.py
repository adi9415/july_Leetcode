# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        p2,p3,p5 = 0,0,0
        
        count = 1
        res = [1]*n
        
        while(count<n):
            minimum = min(res[p2]*2,res[p3]*3,res[p5]*5)
            res[count] = minimum
            count += 1
            if minimum == res[p2]*2:
                p2 += 1
            if minimum == res[p3]*3:
                p3 += 1
            if minimum == res[p5]*5:
                p5 += 1
            
        
        return res[n-1]
        