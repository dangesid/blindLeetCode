# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


"""

lst = []
list_1 = [1,2,3,4,5,6]

lst.append([list_1[2]])
lst.append(list_1)
print(lst)
"""

strs = ["eat","tea","tan","ate","nat","bat"]


def count_characters(word):
    # Create a frequency dictionary for characters in the word
    count = {}
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


def group_anagrams(words):
    anagrams = {}

    for word in words:
        # Get character count for the word
        char_count = count_characters(word)

        # Convert character count dictionary to a tuple of sorted (char, count) pairs
        char_count_key = tuple(sorted(char_count.items()))

        # If the tuple key is already in the dictionary, append the word to its list
        if char_count_key in anagrams:
            anagrams[char_count_key].append(word)
        else:
            # Otherwise, create a new list with the current word
            anagrams[char_count_key] = [word]

    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())


# Example usage:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped_anagrams = group_anagrams(words)
print(grouped_anagrams)
