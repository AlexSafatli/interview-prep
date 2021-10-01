class Node(object):
    def __init__(self, dat):
        self.data = dat
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size: int = 0

    def __len__(self):
        return self.size

    @property
    def tail(self):
        if self.head is None:
            return None
        cursor = self.head
        while cursor.next is not None:
            cursor = cursor.next
        return cursor

    def append_node_to_head(self, n: Node):
        if self.head is not None:
            cursor = self.head
            n.next = cursor
        self.head = n
        self.size += 1

    def append_to_head(self, dat):
        n = Node(dat)
        self.append_node_to_head(n)
        return n

    def append_node_to_tail(self, n: Node):
        if self.head is None:
            self.head = n
            return
        cursor = self.tail
        cursor.next = n
        self.size += 1

    def append_to_tail(self, dat):
        n = Node(dat)
        self.append_node_to_tail(n)
        return n

    def delete_node(self, n: Node):
        cursor = self.head
        if cursor is not None:
            if cursor == n:
                self.head = cursor.next
                self.size -= 1
                return
            while cursor.next is not None:
                if cursor.next == n:
                    cursor.next = cursor.next.next
                    self.size -= 1
                    return
                cursor = cursor.next
        raise Exception('Node not in list')

    def remove_duplicates(self):
        cursor = self.head
        prev = None
        dups = {}
        if cursor is None:
            return
        while cursor is not None:
            if cursor.data in dups:
                # Delete this node (it is a duplicate)
                prev.next = cursor.next
                self.size -= 1
            else:
                dups[cursor.data] = True
                prev = cursor
            cursor = cursor.next

    def __str__(self) -> str:
        s: str = ''
        cursor = self.head
        if cursor is not None:
            while cursor.next is not None:
                s += str(cursor.data) + ' -> '
                cursor = cursor.next
            s += str(cursor.data)
        return s


class Adder(object):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.li_a = LinkedList()
        self.li_b = LinkedList()
        for digit in str(a):
            self.li_a.append_to_head(digit)
        for digit in str(b):
            self.li_b.append_to_head(digit)

    @staticmethod
    def _add(n_a: Node, n_b: Node, carry: int):
        if n_a is None and n_b is None:
            return None

        # Make new node
        result = Node(carry)
        ans = carry

        # Check either node
        if n_a is not None:
            ans += int(n_a.data)
        if n_b is not None:
            ans += int(n_b.data)
        result.data = ans % 10

        # Recurse
        result.next = Adder._add(n_a.next if n_a is not None else None,
                                 n_b.next if n_b is not None else None,
                                 int(ans/10))
        return result

    def add(self) -> LinkedList:
        ans = LinkedList()
        if self.li_a.head is None:
            return self.li_b
        if self.li_b.head is None:
            return self.li_a
        ans.head = Adder._add(self.li_a.head, self.li_b.head, 0)
        return ans


if __name__ == '__main__':
    l: LinkedList = LinkedList()
    l.append_to_tail('door')
    node = l.append_to_tail('car')
    l.append_to_tail('bee')
    l.append_to_tail('vee')
    l.delete_node(node)
    l.append_to_tail('bee')
    l.append_to_tail('bee')
    l.remove_duplicates()
    print(l)
    print('=' * 30 + '\n' + str(l) + '\n' + '=' * 30)
    a = Adder(120, 29)
    print(str(a.add()) + '\n' + '=' * 30)
