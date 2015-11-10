package structures;
import structures.HashTable;
import structures.LinkedList;
import structures.Node;

public class Graph {
 
  private HashTable<Integer,LinkedList<Integer>> adjacency;
  private int size;

  public Graph() {
    adjacency = new HashTable<Integer,LinkedList<Integer>>();
  }

  public boolean adjacent(int a, int b) {
    LinkedList<Integer> edges = adjacency.get(a);
    return (edges.contains(b));
  }

}