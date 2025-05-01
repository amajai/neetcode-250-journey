"""
Difficulty: [Easy]
NeetCode #: [9/250]
Date Solved: [01/05/25]
Attempt: [First Attempt]
Revision: 0 (MOST REVISE)

Approach:
- When loop through the numbers, keep track of the count in hashmap or using Boyer-Moore Voting Algorithm

Time Complexity: O(n/k) # Number of keys / size of the set 
Space Complexity: O(k + m) # Number of unique keys plus set

Key Insights:
- When there is set limit of calls (ex: 10^4), can go for a simplier way.
- Uncertain number of calls, use the linked list method
"""
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return 
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)