# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 2^31.



class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
Solution 1:   
        res = x^y
        
        count = 0
        
        while(res):
            if (res & 1):
                count +=1
            res = res>>1
                
        return count
    
Solution 2
    c = 0
        i = 0
        
        while(i<32):
            if (x&1 ^ y&1 != 0):
                c += 1
            x = x>>1
            y = y>>1
            i+= 1
        return c