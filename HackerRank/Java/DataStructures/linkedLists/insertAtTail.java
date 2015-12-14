class Solution {
	Node Insert(Node head,int data) {
		Node current = head;
    		Node new_node = new Node();
    		new_node.data = data;
    		if (head == null) return new_node;
    		while (current.next != null) current = current.next;
    		current.next = new_node;
    		return head;
	}
}
