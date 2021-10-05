# Review: http://en.wikipedia.org/wiki/Binary_search_tree --> Insertion ***

# (Binary) Tree Traversals: (1) In-Order, (2) Pre-Order, (3) Post-Order
#                           (1) left, root, right
#                           (2) root, left, right
#                           (3) left, right, root
# Graph Traversals: (1) Depth First Search, (2) Breadth First Search
# Check if tree is balanced: (maxDepth - minDepth <= 1)

import typing


class IntegerBinarySearchTreeNode(object):
    def __init__(self, dat):
        self.data = dat
        self.left: typing.Optional[IntegerBinarySearchTreeNode] = None
        self.right: typing.Optional[IntegerBinarySearchTreeNode] = None

    def insert(self, i: int):
        if i > self.data:
            # Insert right
            if self.right is None:
                self.right = IntegerBinarySearchTreeNode(i)
            else:
                self.right.insert(i)
        else:
            # Insert left
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


# Minimal height BST
def generate_minimal_height_bst(arr: typing.List[int]
                                ) -> IntegerBinarySearchTreeNode:
    return get_midpt_of_array_as_node(arr, 0, len(arr)-1)


def get_midpt_of_array_as_node(arr: typing.List[int], start: int, end: int) -> \
        typing.Optional[IntegerBinarySearchTreeNode]:
    if end < start:
        return None
    mid = int((end + start) / 2)
    cur = IntegerBinarySearchTreeNode(arr[mid])
    cur.left = get_midpt_of_array_as_node(arr, start, mid - 1)
    cur.right = get_midpt_of_array_as_node(arr, mid + 1, end)
    return cur


if __name__ == '__main__':
    print(generate_minimal_height_bst(list(range(2, 7))))

