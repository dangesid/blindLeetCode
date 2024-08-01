# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
import re
s = "A man, a plan, a canal: Panama"
# s = s.lower()
# s_strip = s.replace(" ","")
# print(s_strip)
#
# s_strip = re.sub(",","",s_strip)
# s_strip = re.sub(":","",s_strip)
#
# print(s_strip)
#
# if s_strip == s_strip[::-1]:
#     print("Palindorme")
# else:
#     print("Not a Palindrome")


s = ''.join(char.lower() for char in s if char.isalnum())
if s == s[::-1]:
    print(True)
else:
    print(False)