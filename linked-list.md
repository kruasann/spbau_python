# Linked List

+ [Reverse Linked List
](#reverse-linked-list
)
## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode


class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur is not None:
            result.append(cur.val)
            cur = cur.next
        return result

    def create_linked_list(self, values):
        values.reverse()
        if not values:
            return None
        prev_node = ListNode(values[0])
        for i in range(1, len(values)):
            next_node = ListNode(values[i], prev_node)
            prev_node = next_node
        return prev_node

    def test_empty_list(self):
        result = self.solution.reverseList(ListNode())
        expected = ListNode()
        self.assertEqual(self.get_linked_list_values(result), self.get_linked_list_values(expected))

    def test_one_value(self):
        result = self.solution.reverseList(ListNode(1))
        expected = ListNode(1)
        self.assertEqual(self.get_linked_list_values(result), self.get_linked_list_values(expected))

    def test_two_values(self):
        head = self.create_linked_list([11, 5, 38, 2, 9])
        result = self.solution.reverseList(head)
        self.assertEqual(self.get_linked_list_values(result), [9, 2, 38, 5, 11])


if __name__ == "__main__":
    unittest.main()
 ```

</blockquote></details>

```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        if head is None:
            return head
            
        cur_node = head
        prev_node = None
            
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            head = prev_node
            
        return head
```

