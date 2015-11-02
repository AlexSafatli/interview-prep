import structures.Stack;

public class StackBasedQueue<T> {

  private Stack<T> oldest, newest;

  public StackBasedQueue() {
    oldest = new Stack<T>();
    newest = new Stack<T>();
  }

  private void shift() {
    while (newest.size() > 0) oldest.push(newest.pop());
  }

  public int size() {
    return oldest.size() + newest.size();
  }

  public void enqueue(T data) {
    newest.push(data);
  }

  public T dequeue() {
    shift();
    return oldest.pop();
  }

  public static void main(String[] args) {
    StackBasedQueue<Integer> queue = new StackBasedQueue<Integer>();
    queue.enqueue(2); queue.enqueue(3); queue.enqueue(100);
    System.out.println(queue.dequeue());
  }

}