# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        str_reverse = str(x)[::-1]
        
        if str_reverse.isalnum():
            int_reverse = int(str_reverse)
            
            if int_reverse > -2 ** 31 and int_reverse < 2 ** 31 - 1:
                return int_reverse
            else:
                return 0
        else:
            int_reverse = -int(str_reverse[0:len(str_reverse) - 1])
            
            if int_reverse > -2 ** 31 and int_reverse < 2 ** 31 - 1:
                return int_reverse
            else:
                return 0
