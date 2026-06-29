"""
Problem: 2. Add Two Numbers
Difficulty: Medium
Language: Python

Approach:
- Traverse both linked lists simultaneously.
- At each step, add the corresponding digits along with any carry from
  the previous addition.
- Create a new node containing the current digit (total % 10).
- Update the carry (total // 10).
- Continue until both linked lists have been fully processed and there
  is no remaining carry.

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

LeetCode:
https://leetcode.com/problems/add-two-numbers/
"""

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Dummy node simplifies construction of the result linked list.
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Continue while there are remaining digits or a carry.
        while l1 or l2 or carry:

            # Use 0 if a list has already been exhausted.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            # Compute the new carry and the digit to store.
            carry = total // 10
            digit = total % 10

            # Append the new digit to the result list.
            current.next = ListNode(digit)
            current = current.next

            # Advance through the input lists if possible.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the head of the constructed list.
        return dummy.next
