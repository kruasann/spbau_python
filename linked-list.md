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

    def test_empty_list(self):
        result = self.solution.reverseList(ListNode())
        expected = ListNode()
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(expected))

    def test_one_value(self):
        result = self.solution.reverseList(ListNode(1))
        expected = ListNode(1)
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(expected))

    def test_two_values(self):
        two = ListNode(2)
        one = ListNode(1, two)
        two_res = ListNode(1)
        one_res = ListNode(2, two_res)
        result = self.solution.reverseList(one)
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(one_res))


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
        values = self.get_linked_list_values(head)
        values.reverse()
        head1 = self.create_linked_list(values)
        return head1

    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return result

    def create_linked_list(self, values):
        values.reverse()
        if values == []:
            return None
        prev_node = ListNode(values[0])
        for i in range(1, len(values)):
            next_node = ListNode(values[i], prev_node)
            prev_node = next_node
        return prev_node
```

