class Solution {
	void Print(Node head) {
		Node current = head;
		while (current != null) { System.out.println(current.data); current = current.next; }
	}
	public static void main(String[] args) {
		LinkedList list = new LinkedList<Integer>();
		list.appendToTail(1);
		list.appendToTail(2);
		list.appendToTail(3);
		Print(list.getHead()); // Prints 1\n2\n3\n
	}
}
