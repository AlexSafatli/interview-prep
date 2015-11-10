package main

/* Node */
type Node struct {
  next *Node
  data int
  key int
}

func NewNode(key int, data int) *Node {
  n := new(Node)
  n.data = data
  n.key = key
  return n
}

/* Linked List */
type SymbolTable struct {
  head *Node
  size int
}

func NewSymbolTable() *SymbolTable {
  l := new(SymbolTable)
  return l
}

func (list *SymbolTable) GetTail() *Node {
  if (list.head == nil) {
    return nil
  }
  var cursor *Node = list.head
  for ; cursor.next != nil ; {
    cursor = cursor.next
  }
  return cursor
}

func (list *SymbolTable) Put(key int, data int) {
  n := NewNode(key, data)
  list.AppendNodeToTail(n)
}

func (list *SymbolTable) AppendNodeToTail(node *Node) {
  if (list.head == nil) {
    list.head = node
  } else {
    list.GetTail().next = node
  }
  list.size++
}

func (list *SymbolTable) Get(key int) int {
  if (list.head == nil) {
    return -1
  }
  var cursor *Node = list.head
  for ; cursor != nil ; cursor = cursor.next {
    if (cursor.key == key) {
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
