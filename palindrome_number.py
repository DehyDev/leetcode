# https://leetcode.com/problems/palindrome-number/submissions/

class Solution(object):
    def isPalindrome(self, x):
        if x >= 0: return int(str(x)[::-1]) == x
