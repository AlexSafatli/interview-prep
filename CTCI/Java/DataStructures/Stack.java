package structures;
import structures.LinkedList;

public class Stack<T> {

  private LinkedList<T> elements;

  public Stack() {
    elements = new LinkedList<T>();
  }

  public int size() {
    return elements.size();
  }

  public T pop() {
    return elements.removeHead();
  }

  public T peek() {
    return (size() > 0) ? elements.getHead().getData() : null;
  }

  public void push(T data) {
    elements.appendToHead(data);
  }

  public static void main(String[] args) {
    Stack<Integer> stack = new Stack<Integer>();
    stack.push(2); stack.push(3);
    System.out.println(stack.peek());
    System.out.println(stack.pop());
    System.out.println(stack.pop());
  }

}