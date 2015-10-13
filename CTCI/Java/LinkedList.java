public class LinkedList<T> {
	
	private Node<T> head;
	private int size;

	public LinkedList() {
		head = null;
	}

	public LinkedList(T[] arr) {
		super();
		for (int i = 0; i < arr.length; ++i) add(arr[i]);
	}

	public Node<T> getHead() {
		return head;
	}

	public int getSize() {
		return size;
	}

	public Node<T> appendToHead(T data) {
		Node<T> n = new Node<T>(data);
		appendNodeToHead(n);
		return n;
	}

	public void appendNodeToHead(Node<T> node) {
		if (head != null) {
			node.setNext(head);
		}
		head = node;
		++size;
	}

	public Node<T> getTail() {
		Node<T> cursor = getHead();
		if (cursor == null) return null;
		while (cursor.getNext() != null) {
			cursor = cursor.getNext();
		}
		return cursor;
	}

	public Node<T> appendToTail(T data) {
		Node<T> n = new Node<T>(data);
		appendNodeToTail(n);
		return n;
	}

	public Node<T> add(T data) {
		return appendToTail(data);
	}

	public void appendNodeToTail(Node<T> node) {
		if (head == null) head = node;
		else {
			Node<T> cursor = getTail();
			cursor.setNext(node);
		}
		++size;
	}

	public void deleteNode(Node<T> node) {
		Node<T> cursor = head;
		if (cursor != null) {
			if (cursor.equals(node)) {
				head = cursor.getNext();
				--size;
				return;
			}
			while (cursor.getNext() != null) {
				if (cursor.getNext().equals(node)) {
					cursor.setNext(cursor.getNext().getNext());
					--size;
					return;
				}
				cursor = cursor.getNext();
			}
			throw new RuntimeException("Node not found in list.");
		}
	}

	public static void main(String[] args) {
		Integer[] arr = { 3, 4, 5 };
		LinkedList<Integer> intList = new LinkedList<Integer>();
		intList.add(2);
		intList.add(10);
		intList.appendToHead(8);
		intList.deleteNode(intList.getTail());
		System.out.println(intList.getSize());
		intList = new LinkedList<Integer>(arr);
		System.out.println(intList.getSize());
	}

}