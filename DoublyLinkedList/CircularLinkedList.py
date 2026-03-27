class Node:
    def __init__(self, value=None):
        self.info = value
        self.next = None   # Only ONE pointer (no prev, it's not doubly linked)


class CircularLinkedList:
    def __init__(self):
        self.head = None


    # ── Insert at beginning ──────────────────────────────────────────────
    def insertAtBeg(self, value):
        temp = Node(value)

        if self.head is None:          # List is empty
            self.head = temp
            temp.next = self.head      # Points to itself → circle!
            return

        # Find the last node (the one whose .next == head)
        t = self.head
        while t.next != self.head:
            t = t.next

        # Wire the new node in at the front
        temp.next = self.head          # new → old head
        t.next    = temp               # last → new node (keeps the circle)
        self.head = temp               # move head to new node


    # ── Insert in middle (after node with value x) ───────────────────────
    def insertAtMid(self, value, x):
        t = self.head

        while t.next != self.head:     # stop before going all the way around
            if t.info == x:
                break
            t = t.next

        temp      = Node(value)
        temp.next = t.next             # new node points to what came after x
        t.next    = temp               # x now points to the new node


    # ── Insert at end ────────────────────────────────────────────────────
    def insertAtEnd(self, value):
        temp = Node(value)

        if self.head is None:          # Empty list
            self.head = temp
            temp.next = self.head      # Circle with one node
            return

        t = self.head
        while t.next != self.head:     # Walk until the last node
            t = t.next

        t.next    = temp               # last → new node
        temp.next = self.head          # new node → head  (closes the circle)


    # ── Delete a node ────────────────────────────────────────────────────
    def deleteCLL(self, value):
        if self.head is None:
            print("List is empty")
            return

        t = self.head

        # Special case: deleting the head
        if t.info == value:
            if t.next == self.head:    # Only one node in the list
                self.head = None
                return

            # Find last node so we can re-link it to the new head
            last = self.head
            while last.next != self.head:
                last = last.next

            self.head  = self.head.next   # advance head
            last.next  = self.head        # last still points to head
            return

        # General case: find the node just before the target
        while t.next != self.head:
            if t.next.info == value:
                t.next = t.next.next      # skip over the target node
                return
            t = t.next

        print(f"Value {value} not found")


    # ── Print all nodes ──────────────────────────────────────────────────
    def printCLL(self):
        if self.head is None:
            print("List is empty")
            return

        t = self.head
        while True:
            print(t.info)
            t = t.next
            if t == self.head:            # back to the start → stop
                break


# ── Demo ─────────────────────────────────────────────────────────────────
obj = CircularLinkedList()
obj.insertAtBeg(5)
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtMid(25, 20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.deleteCLL(40)
obj.printCLL()   # → 5, 10, 20, 25, 30