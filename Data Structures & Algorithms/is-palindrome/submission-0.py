class Solution:
    def isPalindrome(self, s: str): #-> bool:
        is_palindrome = False
        #string prep
        s = "".join([char for char in s if char.isalnum()]).lower()
        
        if s == s[::-1]:
            is_palindrome = True
        return is_palindrome
        
        