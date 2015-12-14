class Solution {
	Node InsertNth(Node head, int data, int position) {
    		Node current = head;
    		Node prev = null;
    		int pos = 0;
   		Node input = new Node();
    		input.data = data;
    		if (position == 0) {
        		input.next = head;
        		return input;
    		}
    		while (pos < position) {
        		++pos;
        		prev = current;
        		current = current.next;
    		}
    		if (prev != null) prev.next = input;
    		input.next = current;
    		return head;
	}
}
