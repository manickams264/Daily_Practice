class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary_string = ''
        while head:
            binary_string += str(head.val)
            head = head.next
        return int(binary_string, 2)