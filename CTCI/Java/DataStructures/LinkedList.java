package structures;

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

	public Node<T> getKthToLastNode(int k) {
		// @todo Implement (CTCI 2.2)
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

	public T removeHead() {
		if (head == null) return null;
		T data = head.getData();
		head = head.getNext();
		--size;
		return data;
	}

	public T removeTail() {
		if (head == null) return null;
		Node<T> cursor = head, prev = null;
		while (cursor.getNext() != null) {
			prev = cursor;
			cursor = cursor.getNext();
		}
		if (prev != null) prev.setNext(null);
		else head = null;
		--size;
		return cursor.getData();
	}

	// CTCI 2.3
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

	public void removeDuplicates() {
		// @todo Implement (CTCI 2.1)
	}

	public String toString() {
		String str = "";
		Node<T> cursor = head;
		while (cursor != null) {
			str += cursor.getData().toString();
			if (cursor.getNext() != null) str += " ";
			cursor = cursor.getNext();
		}
		return str;
	}

	public static void main(String[] args) {
		Integer[] arr = { 3, 4, 5 };
		LinkedList<Integer> intList = new LinkedList<Integer>();
		intList.appendToTail(2);
		intList.appendToTail(10);
		intList.appendToHead(98);
		intList.appendToHead(99);
		intList.appendToHead(100);
		System.out.println("List: " + intList);
		System.out.println("Removing Head: " + intList.removeHead());
		System.out.println("Removing Tail: " + intList.removeTail());
		intList.deleteNode(intList.getTail());
		System.out.println("After Removing Tail, Size Is: " + intList.getSize());
		System.out.println("List: " + intList);
	}

}