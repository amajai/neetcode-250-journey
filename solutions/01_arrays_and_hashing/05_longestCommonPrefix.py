"""
Difficulty: [Easy]
NeetCode #: [5/250]
Date Solved: [26/04/25]
Attempt: [Second Attempt]
Revision: 1

Approach:
- Set the first word as base prefix and go through the rest of the words in the array. Match the characters index by index with base and 
current word in loop. Once the characters are no longer the same, change the base prefix to a new one matches both the base and the 
current word. Then move on to the next word and repeat the process until reaching the end of the array with the final base prefix.

Time Complexity: O(n * m) # n is length of strings and m is length of shortest string (pref)
Space Complexity: O(1) # No space/storage used

Key Insights:
- Need to start with the first word in array as reference or current prefix
- Loop in an array of strings, starting from the second string.
- Compare current prefix with string by index. If index in prefix and string are the same while its length are less is both of them continue to loop.
- Once out the loop, make the new prefix from start to position of index and continue to the next word sting
"""


def longestCommonPrefix(strs) -> str:
    pref = strs[0]

    for w in strs[1:]:
        i = 0
        while i < len(pref) and i < len(w) and pref[i] == w[i]:
            i += 1
        pref = pref[:i]
        if not pref: # if pref empty
            return pref
    return pref
