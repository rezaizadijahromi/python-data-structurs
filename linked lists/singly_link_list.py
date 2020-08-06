class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            # print(cur_node.next)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, pre_node, data):
        if not pre_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next = pre_node.next
        pre_node.next = new_node

    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None

        pre_node = None
        while curr_node is not None and curr_node.data != key:
            pre_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        pre_node.next = curr_node.next
        curr_node = None

    def delete_node_with_position(self, pos):
        curr_node = self.head

        if pos == 0:
            self.head = curr_node.next
            curr_node = None

        pre_node = None
        count = 1
        while curr_node and count != pos:
            pre_node = curr_node
            curr_node = curr_node.next
            count += 1

        if curr_node is None :
            message = print("Index out of range")
            return message

        pre_node.next = curr_node.next
        curr_node = None

    def len_iterative(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        
        return 1 + self.len_recursive(node.next)





llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(llist.len_recursive(llist.head))
# llist.insert_after_node(llist.head.next, "E")
#llist.delete_node("C")
# llist.delete_node_with_position(3)

# llist.print_list()