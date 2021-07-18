# https://leetcode.com/problems/palindrome-number/submissions/

class Solution(object):
    def isPalindrome(self, x):
        return x >= 0 and int(str(x)[::-1]) == x
