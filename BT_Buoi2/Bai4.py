class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def __sizeof__(self):
        if self.head == None:
            return 0
        cnt = 0
        temp = self.head
        while temp:
            cnt += 1
            temp = temp.next
        return cnt

    def findmiddleelement(self):
        if self.head == None:
            return None
        pos = int(self.__sizeof__() / 2)
        cnt = 1
        temp = self.head
        if cnt == pos:
            return temp
        while temp:
            cnt += 1
            temp = temp.next
            if cnt == pos:
                return temp

    def __str__(self):
        temp = self.head
        ans = '';
        ans += temp.__str__()
        temp = temp.next
        while temp:
            ans += '->' + temp.__str__()
            temp = temp.next
        return ans

    def __rshift__(self, k):
        size = self.__sizeof__()
        k = k % size
        if k != 0:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = self.head
            for i in range(size - k - 1):
                self.head = self.head.next
            tail = self.head
            self.head = self.head.next
            tail.next = None


linked_list = LinkedList()
linked_list.add_to_tail(Node(1))
linked_list.add_to_tail(Node(2))
linked_list.add_to_tail(Node(3))
linked_list.add_to_tail(Node(4))
linked_list.add_to_tail(Node(5))
linked_list.add_to_tail(Node(6))
linked_list.add_to_tail(Node(7))

print(linked_list.__str__())
print("middle element:",linked_list.findmiddleelement())
linked_list.__rshift__(1)
print(linked_list.__str__())
first = linked_list.remove_from_head()
print("removed:", first)
print(linked_list.__str__())

