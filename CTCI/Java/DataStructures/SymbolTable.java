package structures;

public class SymbolTable<T,K> {

  private Node head;
  private int size = 0;

  private class Node {
    public K key;
    public T data;
    public Node next;
    public Node(K key, T data, Node next) {
      this.key = key; this.data = data; this.next = next;
    }
  }

  public int size() {
    return size;
  }

  public boolean contains(K key) {
    return get(key) != null;
  }

  public T get(K key) {
    for (Node cursor = head; cursor != null; cursor = cursor.next)
      if (key.equals(cursor.key)) return cursor.data;
    return null;
  }

  public void put(K key, T data) {
    if (data == null) {
      delete(key); return;
    }
    for (Node cursor = head; cursor != null; cursor = cursor.next)
      if (key.equals(cursor.key)) {
        cursor.data = data; return;
      }
    head = new Node(key, data, head);
    ++size;
  }

  public static void main(String[] args) {
  }

}