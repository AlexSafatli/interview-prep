import typing

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


# @REP LargestStack on InterviewCake
# A MinStack is similar to a MaxStack. Similar principle.
class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack: Stack = Stack()

    def min(self) -> typing.Optional[int]:
        return self.min_stack.peek()

    def pop(self) -> typing.Optional[int]:
        dat = super().pop()
        if self.min() == dat:
            self.min_stack.pop()
        return dat

    def push(self, dat: int):
        if len(self.min_stack) > 0:
            if self.min() >= dat:
                self.min_stack.push(dat)
        else:
            self.min_stack.push(dat)
        super().push(dat)


if __name__ == '__main__':
    s = Stack()
    s.push('Door')
    s.push('Car')
    print('Stack:', s)
    print(s.pop())
    print(s)
    q = Queue()
    q.enqueue('Door')
    q.enqueue('Car')
    print('Queue:', q)
    print(q.dequeue())
    print(q)
    ms = MinStack()
    ms.push(3)
    ms.push(1)
    ms.push(2)
    print('MinStack:', ms)
    print('Min:', ms.min())
    print('Popped:', ms.pop())
    print('Min:', ms.min())
