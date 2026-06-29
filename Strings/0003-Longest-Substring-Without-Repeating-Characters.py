"""
Problem: 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Language: Python

Approach:
- Use a sliding window to maintain a substring with unique characters.
- Store the most recent index of each character in a dictionary.
- If a duplicate character is encountered within the current window,
  move the left pointer just past its previous occurrence.
- Update the maximum window size throughout the traversal.

Time Complexity: O(n)
Space Complexity: O(min(n, m))

Where:
- n = length of the string
- m = size of the character set

LeetCode:
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Maps each character to its most recent index.
        char_index = {}

        longest = 0
        left = 0  # Left boundary of the current sliding window.

        for right, char in enumerate(s):

            # If the character is already inside the current window,
            # move the left boundary past its previous occurrence.
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            # Update the character's most recent position.
            char_index[char] = right

            # Update the maximum window length found so far.
            longest = max(longest, right - left + 1)

        return longest
