package structures;
import structures.LinkedList;
import structures.SymbolTable;

public class HashTable<K,T> {

  private static final int INIT_CAPACITY = 13;
  private SymbolTable<K,T>[] values;
  private int capacity;

  public HashTable() {
    this(INIT_CAPACITY);
  }

  public HashTable(int capacity) {
    this.capacity = capacity;
    keys = new LinkedList<K>();
    values = (SymbolTable<K,T>[]) new SymbolTable[capacity];
    for (int i = 0; i < capacity; ++i) values[i] = new SymbolTable<K,T>();
  }

  public T get(K key) {
    return values[hash(key)].get(key);
  }

  public void put(K key, T value) {
    values[hash(key)].put(key, value);
  }

  public void delete(K key) {
    values[hash(key)].delete(key);
  }

  private int hash(K key) {
    return ((key.hashCode() & 0x7fffffff) % capacity);
  }

  public static void main(String[] args) {
    HashTable<String,Integer> hash = new HashTable<String,Integer>();
    hash.put("door",2);
    System.out.println(hash.get("door"));
  }

}