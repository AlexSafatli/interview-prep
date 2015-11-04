package structures;
import java.util.Map;
import java.util.HashMap;
import structures.Edge;

public class Graph {
 
  private Map<Integer,Edge> adjacency;
  private int size;

  public Graph() {
    adjacency = new HashMap<Integer,Edge>();
  }

}