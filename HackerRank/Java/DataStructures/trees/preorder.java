class Solution {
	void Preorder(Node root) {
    		if (root == null) return;
	 	System.out.print(root.data);
		// Probably could be done better without repetitive code.
    		Recurse(root.left);
    		Recurse(root.right);
	}
	void Recurse(Node root) {
    		if (root == null) return;
    		System.out.print(" " + root.data);
    		Recurse(root.left);
    		Recurse(root.right);
	}
}
