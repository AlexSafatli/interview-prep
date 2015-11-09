package structures;
import structures.LinkedList;
import structures.SymbolTable;

public class HashTable<K,T> {

  private static final int INIT_CAPACITY = 13;
  private LinkedList<K> keys;
  private SymbolTable<K,T>[] values;
  private int capacity;
  private int size = 0;

  public HashTable() {
    this(INIT_CAPACITY);
  }

  public HashTable(int capacity) {
    this.capacity = capacity;
    keys = new LinkedList<K>();
    values = (SymbolTable<K,T>[]) new SymbolTable[capacity];
  }

  public T get(K key) {
    return values[hash(key)].get(key);
  }

  public void put(K key, T value) {
    int hash = hash(key);
    if (values[hash] == null) {
      values[hash] = new SymbolTable<K,T>();
    }
    values[hash].put(key, value);
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