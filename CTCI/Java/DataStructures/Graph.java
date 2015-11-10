package structures;
import structures.HashTable;
import structures.Node;

public class Graph {
 
  private HashTable<Integer,Edge> adjacency;
  private int size;

  private class Edge {
    // @todo Implement
  }

  public Graph() {
    adjacency = new HashTable<Integer,Edge>();
  }

}