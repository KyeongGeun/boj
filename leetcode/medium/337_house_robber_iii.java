class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Pair {
    int include;
    int except;

    Pair(int include, int except) {
        this.include = include;
        this.except = except;
    }
}

class Solution {
    public Pair recur(TreeNode node) {
        int include = node.val, except = 0;

        if (node.left != null) {
            Pair pair = recur(node.left);
            include += pair.except;
            except += Math.max(pair.include, pair.except);
        }
        if (node.right != null) {
            Pair pair = recur(node.right);
            include += pair.except;
            except += Math.max(pair.include, pair.except);
        }

        return new Pair(include, except);
    }

    public int rob(TreeNode root) {
        Pair pair = recur(root);

        return Math.max(pair.include, pair.except);
    }
}
