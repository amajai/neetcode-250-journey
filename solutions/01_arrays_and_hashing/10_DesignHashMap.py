"""
Difficulty: [Easy]
NeetCode #: [10/250]
Date Solved: [02/05/25]
Attempt: [First Attempt]
Revision: 0

Approach:
- Very similar to Hashset approach, which is to use linked list with dummy node but thise time, to make custom hashmap method. All 
step are the similar with difference of including value to the dummy node (ListNode) class constructor.

Time Complexity: O(n/k) # Number of keys / size of the set 
Space Complexity: O(k + m) # Number of unique keys plus set

Key Insights:
- When there is set limit of calls (ex: 10^4), can go for a simplier way.
- Uncertain number of calls, use the linked list method
"""

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [ListNode(-1,-1) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        cur = self.map[key % len(self.map)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[key % len(self.map)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1
    

    def remove(self, key: int) -> None:
        cur = self.map[key % len(self.map)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)