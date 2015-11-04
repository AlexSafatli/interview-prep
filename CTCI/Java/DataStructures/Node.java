package structures;

public class Node<T> {
	
	private Node<T> next;
	private T data;
	boolean visited;

	public Node() {
		next = null; data = null;
	}

	public Node(T d) {
		next = null; data = d;
	}

	public T getData() {
		return data;
	}

	public void setData(T d) {
		data = d;
	}

	public Node<T> getNext() {
		return next;
	}

	public void setNext(Node<T> node) {
		next = node;
	}

	public boolean equals(Object other) {
		Node<T> node = (Node<T>)other;
		T odata = (T)node.getData();
		return (odata.equals(data));
	}

}