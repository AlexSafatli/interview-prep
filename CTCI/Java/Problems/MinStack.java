import structures.Stack;
// (REP LargestStack on InterviewCake)
// A MinStack is similar to a MaxStack. Similar principle.
public class MinStack extends Stack<Integer> {

  private Stack<Integer> minStack;

  public MinStack() {
    super();
    minStack = new Stack<Integer>();
  }

  public Integer min() {
    return minStack.peek();
  }

  public Integer pop() {
    Integer data = super.pop();
    if (min() == data) minStack.pop();
    return data;
  }

  public void push(Integer data) {
    if (minStack.size() > 0) {
      if (min() >= data) {
        minStack.push(data);
      }
    } else minStack.push(data);
    super.push(data);
  }

  public static void main(String[] args) {
    MinStack stack = new MinStack();
    stack.push(2); stack.push(3); stack.push(1);
    System.out.println(stack.min());
    System.out.println(stack.pop());
    System.out.println(stack.min());
  }

}