# Input: s = "hello"
# Output: "holle"

s = 'hello'
vowels = 'aeiouAEIOU'

vowels_idices = [i for i,char in enumerate(s) if char in vowels]
vowels_chars = [s[i] for i in vowels_idices]

print(vowels_chars)
print(vowels_idices)
vowels_idices.reverse()
s_lst = list(s)
for index,vowel_index in enumerate(vowels_idices):
    s_lst[vowel_index] = vowels_chars[index]
print("".join(s_lst))