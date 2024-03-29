# Review: http://en.wikipedia.org/wiki/Binary_search_tree --> Insertion ***

# (Binary) Tree Traversals: (1) In-Order, (2) Pre-Order, (3) Post-Order
#                           (1) left, root, right
#                           (2) root, left, right
#                           (3) left, right, root
# Graph Traversals: (1) Depth First Search, (2) Breadth First Search
# Check if tree is balanced: (maxDepth - minDepth <= 1)

import typing
import random


class IntegerBinarySearchTreeNode(object):
    def __init__(self, dat: int):
        self.data: int = dat
        self.left: typing.Optional[IntegerBinarySearchTreeNode] = None
        self.right: typing.Optional[IntegerBinarySearchTreeNode] = None

    def insert(self, i: int):
        # Definition of a BST is that a given node is < nodes on its right
        # and > nodes on its left.
        if i > self.data:  # Right
            if self.right is None:
                self.right = IntegerBinarySearchTreeNode(i)
            else:
                self.right.insert(i)
        else:  # Left
            if self.left is None:
                self.left = IntegerBinarySearchTreeNode(i)
            else:
                self.left.insert(i)

    def __str__(self) -> str:
        s = '%d (L: %d, R: %d)' % (
            self.data, -1 if self.left is None else self.left.data,
            -1 if self.right is None else self.right.data)
        if self.left is not None:
            s += ' -> \n' + str(self.left)
        if self.right is not None:
            s += ' -> \n' + str(self.right)
        return s


# Minimal height BST is generated by finding midpoint of a sorted array
# and making that the root, then doing the same for the sub-arrays on both
# sides of this midpoint
def generate_minimal_height_bst(arr: typing.List[int]
                                ) -> IntegerBinarySearchTreeNode:
    return get_midpt_of_array_as_node(arr, 0, len(arr)-1)


def get_midpt_of_array_as_node(arr: typing.List[int], start: int, end: int) -> \
        typing.Optional[IntegerBinarySearchTreeNode]:
    if end < start:
        return None
    mid = (end + start) // 2
    cur = IntegerBinarySearchTreeNode(arr[mid])
    cur.left = get_midpt_of_array_as_node(arr, start, mid - 1)
    cur.right = get_midpt_of_array_as_node(arr, mid + 1, end)
    return cur


def gen_range() -> typing.List[int]:
    x = random.randint(0, 99)
    y = random.randint(x, 100)
    nums = list(range(x, y))
    mid = (len(nums)-1)//2
    print('Range(%d,%d):' % (x, y), nums)
    print('Midpoint:', nums[mid])
    return nums


if __name__ == '__main__':
    sorted_li = gen_range()
    print(generate_minimal_height_bst(sorted_li))

