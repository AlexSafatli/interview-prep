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


# @REP LargestStack on InterviewCake
class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.max_stack: Stack = Stack()

    def max(self) -> typing.Optional[int]:
        return self.max_stack.peek()

    def pop(self) -> typing.Optional[int]:
        dat = super().pop()
        if self.max() == dat:
            self.max_stack.pop()
        return dat

    def push(self, dat: int):
        if len(self.max_stack) > 0:
            if self.max() <= dat:
                self.max_stack.push(dat)
        else:
            self.max_stack.push(dat)
        super().push(dat)


# 3.1, Divide the array into 3 parts of equal size. Stack grows in those (limited) spaces.
#  [0,n/3)
#  [n/3,2n/3)
#  [2n/3,n)
# Assumes: no knowledge of space usage. Cannot use any extra space (resizable array?).
# 3.2, Have nodes keep track of min, or Stack class keep track on addition/deletion (problem here is on deletion).
# 3.3, Rollover, see solution. *
# 3.4, Towers of Hanoi (see separate file).


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
    mxs = MaxStack()
    mxs.push(1)
    mxs.push(2)
    mxs.push(3)
    print('MaxStack:', mxs)
    print('Max:', mxs.max())
    print('Popped:', mxs.pop())
    print('Max:', mxs.max())
