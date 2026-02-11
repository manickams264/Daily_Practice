def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev=None
    current=head
    while current:
        nextnode=current.next
        current.next=prev
        prev=current
        current=nextnode
    head=prev
    return head