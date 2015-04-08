package main

/* Node */
type Node struct {
	next *Node
	data int
}

func NewNode(data int) *Node {
	n := new(Node)
	n.data = data
	return n
}

/* Linked List */
type LinkedList struct {
	head *Node
	size int
}

func NewLinkedList() *LinkedList {
	l := new(LinkedList)
	return l
}

func (list *LinkedList) GetTail() *Node {
	if (list.head == nil) {
		return nil
	}
	var cursor *Node = list.head
	for ; cursor.next != nil ; {
		cursor = cursor.next
	}
	return cursor
}

func (list *LinkedList) AppendToTail(data int) {
	n := NewNode(data)
	list.AppendNodeToTail(n)
}

func (list *LinkedList) AppendNodeToTail(node *Node) {
	if (list.head == nil) {
		list.head = node
	} else {
		list.GetTail().next = node
	}
	list.size++
}

/* Main (Test) */
func main() {
	l := NewLinkedList()
	l.AppendToTail(2)
	println(l.head.data)
}
