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

    def node_swap(self, key1, key2):
        if key1 == key2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 is not None and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 is not None and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if curr_1 is None or curr_2 is None:
            return

        if prev_1 is not None:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2 is not None:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def print_helper(self, node, name):
        if node is None:
            print(name + ":None")
        else:
            print(name + ":" + node.data)

    def reverse_iterative(self):
        prev = None
        curr = self.head

        while curr is not None:
            nxt = curr.next
            curr.next = prev

            self.print_helper(prev, "PREV")
            self.print_helper(curr, "CUR")
            self.print_helper(nxt, "NXT")

            prev = curr
            curr = nxt

        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if cur is None:
                return prev
            
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):

        p = self.head
        q = llist.head
        s = None
        if p is None:
            return q
        if q is None:
            return p

        if p is not None and q is not None:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p is not None and q is not None:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if q is None:
            s.next = p
        if p is None:
            s.next = q

        return new_head

    def remove_duplicates(self):
        current = self.head
        pre = None
        dup_values = {}
        while current is not None:
            if current.data in dup_values:
                pre.next = current.next
                current = None
            else:
                dup_values[current.data] = 1
                pre = current

            print(dup_values)
            current = pre.next
    def point_nth_from_last(self, n):
        total_len = self.len_iterative()
        cur = self.head

        while cur is not None:
            if total_len == n:
                print(cur.data)
            total_len -= 1
            cur = cur.next
        if cur is None:
            return

    def point_nth_from_last_sec(self, n):
        p = self.head
        q = self.head

        count = 0
        while q is not None and count < n:
            q = q.next
            count += 1

        if q is None:
            print(f"{n} is greater than number of node in list")
            return

        while p is not None and q is not None:
            p = p.next
            q = q.next

        print(p.data)
        return p.data

    def count_occurences_iterative(self, data):
        current = self.head

        count = 0
        while current is not None:
            if  current.data == data:
                count += 1
            current = current.next

        return count
    
    def count_occurences_recursive(self, node, data):
        if node is None:
            return 0
        
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        p = self.head
        q = self.head
        
        prev = None
        count = 0

        while p is not None and count < k:
            count += 1
            prev = p
            p = p.next
            q = q.next

        p = prev

        while q  is not None:
            prev = q
            q = q.next

        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    def is_palindrome1(self):
        s = ""
        current = self.head
        while current is not None:
            s += current.data
            current = current.next

        return s == s[::-1]
    
    def is_palindrome2(self):
        current = self.head
        s = []

        while current is not None:
            s.append(current.ddata)
            current = current.next

        current = self.head

        while current is not None:
            data = s.pop()
            if current.data == data:
                return True

            current = current.next

        return False

    def is_palindrome3(self):
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q is not None:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]

        count = 1
        while count <= i // 2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

    def move_tail_to_head(self):
        current = self.head

        prev = None
        while current.next is not None:
            prev = current
            current = current.next

        
        current.next = self.head
        prev.next = None
        self.head = current

        # print(prev.data)



Linked1 = LinkedList()

Linked1.append("A")
Linked1.append("B")
Linked1.append("C")
Linked1.append("D")

Linked1.move_tail_to_head()
Linked1.print_list()


# Linked = LinkedList()

# Linked.append("R")
# Linked.append("A")
# Linked.append("D")
# Linked.append("A")
# Linked.append("R")
# print(Linked.is_palindrome1())


# Linked1 = LinkedList()

# Linked1.append("A")
# Linked1.append("B")
# Linked1.append("C")
# print(Linked1.is_palindrome3())



# Linked = LinkedList()
# Linked.append(1)
# Linked.append(2)
# Linked.append(3)
# Linked.append(4)
# Linked.append(5)
# Linked.append(6)

# Linked.print_list()
# print("\n")

# Linked.rotate(4)

# Linked.print_list()


# Linked.append(1)
# Linked.append(2)
# Linked.append(1)
# Linked.append(4)
# Linked.append(7)
# Linked.append(7)
# Linked.append(7)
# print(Linked.count_occurences_iterative(7))
# print(Linked.count_occurences_recursive(Linked.head, 7))



# Linked.append("A")
# Linked.append("B")
# Linked.append("C")
# Linked.append("D")
# Linked.point_nth_from_last_sec(2)
# Linked.point_nth_from_last(2)



# Linked.append(1)
# Linked.append(2)
# Linked.append(1)
# Linked.append(4)
# Linked.append(7)
# Linked.append(7)
# Linked.append(7)
# Linked.append(8)
# Linked.append(6)

# Linked.remove_duplicates()
# Linked.print_list()


# llist1 = LinkedList()
# llist2 = LinkedList()

# llist1.append(1)
# llist1.append(5)
# llist1.append(7)
# llist1.append(9)
# llist1.append(10)

# llist2.append(2)
# llist2.append(3)
# llist2.append(4)
# llist2.append(6)
# llist2.append(8)

# llist1.merge_sorted(llist2)
# llist1.print_list()



# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.reverse_recursive()
# llist.reverse_iterative()
# llist.node_swap("A", "B")
# print(llist.len_recursive(llist.head))
# llist.insert_after_node(llist.head.next, "E")
#llist.delete_node("C")
# llist.delete_node_with_position(3)

# llist.print_list()