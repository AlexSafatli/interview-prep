from linked_lists import LinkedList


class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def pop(self):
        if len(self) > 0:
            top = self.head
            data = top.data
            self.delete_node(top)
            return data
        return None

    def push(self, dat):
        self.append_to_head(dat)

    def peek(self):
        if self.head is None:
            return None
        return self.head.data


class Queue(LinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, dat):
        self.append_to_tail(dat)

    def dequeue(self):
        head = self.head
        if head is not None:
            self.delete_node(head)
            return head.data
        return None


if __name__ == '__main__':
    s = Stack()
    s.push('Door')
    s.push('Car')
    print(s.pop())
    print(s)
    q = Queue()
    q.enqueue('Door')
    q.enqueue('Car')
    print(q.dequeue())
    print(q)
