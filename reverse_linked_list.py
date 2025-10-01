class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reversal(self):
        last = None
        now = self
        next = None
        while True:
            next = now.next
            now.next = last
            last = now
            now = next
            if now == None:
                return last

a3 = ListNode(3, None)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)

print(a1.reversal().next.next.next)
