package structures;
import structures.LinkedList;

public class SymbolTable<K,T> {

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

  public void delete(K key) {
    if (head == null) return;
    if (key.equals(head.key)) {
      head = head.next;
      --size;
      return;
    }
    Node previous = head;
    for (Node cursor = head.next; cursor != null; cursor = cursor.next) {
      if (key.equals(cursor.key)) {
        previous.next = cursor.next;
        --size;
        return;
      }
      previous = cursor;
    }
  }

  public LinkedList<K> keys() { // @todo Convert to iterable.
    LinkedList<K> keys = new LinkedList<K>();
    for (Node cursor = head; cursor != null; cursor = cursor.next) {
      keys.appendToTail(cursor.key);
    }
    return keys;
  }

  public static void main(String[] args) {
  }

}