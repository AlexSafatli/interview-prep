package main

type SymbolTableNode struct {
	next *SymbolTableNode
	data int
	key  int
}

func NewSymbolTableNode(key int, data int) *SymbolTableNode {
	n := new(SymbolTableNode)
	n.data = data
	n.key = key
	return n
}

// SymbolTable (Linked List)
type SymbolTable struct {
	head *SymbolTableNode
	size int
}

func NewSymbolTable() *SymbolTable {
	l := new(SymbolTable)
	return l
}

func (list *SymbolTable) GetTail() *SymbolTableNode {
	if list.head == nil {
		return nil
	}
	var cursor = list.head
	for cursor.next != nil {
		cursor = cursor.next
	}
	return cursor
}

func (list *SymbolTable) Put(key int, data int) {
	n := NewSymbolTableNode(key, data)
	list.AppendNodeToTail(n)
}

func (list *SymbolTable) AppendNodeToTail(node *SymbolTableNode) {
	if list.head == nil {
		list.head = node
	} else {
		list.GetTail().next = node
	}
	list.size++
}

func (list *SymbolTable) Get(key int) int {
	if list.head == nil {
		return -1
	}
	var cursor = list.head
	for ; cursor != nil; cursor = cursor.next {
		if cursor.key == key {
			return cursor.data
		}
	}
	return -1
}

/* Main (Test) */
func main() {
	l := NewSymbolTable()
	l.Put(2, 2)
	println(l.Get(2))
}
