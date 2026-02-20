class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        current_A = headA
        current_B = headB
        while current_A != current_B:
            current_A = current_A.next if current_A else headB
            current_B = current_B.next if current_B else headA
        return current_A