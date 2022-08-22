# Check Palindrome
# Given the string, check if it is a palindrome.
# Example
# For inputString = "aabaa", the output should be
# solution(inputString) = true;
# For inputString = "abac", the output should be
# solution(inputString) = false;
# For inputString = "a", the output should be
# solution(inputString) = true.
# Input/Output
# [execution time limit] 4 seconds (js)
# [input] string inputString
# A non-empty string consisting of lowercase characters.
# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 105.
# [output] boolean
# true if inputString is a palindrome, false otherwise.
def isPalindrome(str):
    if len(str)==1:
        return True
    elif len(str) %2 == 0:
            first_half = str[0:len(str)//2]
            second_half = str[-1:-(len(str)//2)-1:-1]
            if first_half == second_half:
                return  True
            else:     
                return  False
    else:
           first_half = str[0:len(str)//2]
           second_half = str[-1:-len(str)//2:-1]
           if first_half == second_half:
                return  True
           else:     
                return  False    
print(isPalindrome("aabaa"))
print(isPalindrome("abac"))
print(isPalindrome("a"))