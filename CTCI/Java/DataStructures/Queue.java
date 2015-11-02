package structures;
import structures.LinkedList;

public class Queue<T> {

  LinkedList<T> elements;

  public Queue() {
    elements = new LinkedList<T>();
  }

  public int size() {
    return elements.size();
  }

  public T dequeue() {
    return elements.removeHead();
  }

  public void enqueue(T data) {
    elements.appendToTail(data);
  }

  public static void main(String[] args) {
    Queue<Integer> queue = new Queue<Integer>();
    queue.enqueue(2); queue.enqueue(3);
    System.out.println(queue.dequeue());
    System.out.println(queue.dequeue());
  }

}