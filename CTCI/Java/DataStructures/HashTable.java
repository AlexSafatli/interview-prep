package structures;
import LinkedList;

public class HashTable<T,K> {

  private LinkedList<T> keys;
  private LinkedList<K>[] values;
  private int capacity = 13;
  private int size = 0;

  public HashTable<T,K>() {
    keys = new LinkedList<T>();
    values = new LinkedList<K>[capacity];
  }

  public HashTable<T,K>(int capacity) {
    this.capacity = capacity;
    this.super();
  }

  public K get(T key) {
    // @todo Implement
  }

  public void put(T key, K value) {
    values[hash(key)].appendToTail(value);
  }

  private int hash(T key) {
    return ((key.hashCode() & 0x7fffffff) % capacity);
  }

}