import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;

class Solution {

    static class Node implements Comparable<Node> {
        int id;
        int val;

        Node(int id, int val) {
            this.id = id;
            this.val = val;
        }

        @Override
        public int compareTo(Node node) {
            return this.val - node.val;
        }
    }

    public int[] solution(String[] operations) {
        Set<Integer> set = new HashSet<>();
        PriorityQueue<Node> maxQ = new PriorityQueue<>();
        PriorityQueue<Node> minQ = new PriorityQueue<>();

        for (int i = 0; i < operations.length; i++) {
            String s = operations[i];
            String[] ss = s.split(" ");
            if (ss[0].equals("I")) {
                Node node = new Node(i, Integer.parseInt(ss[1]));
                maxQ.add(new Node(i, -node.val));
                minQ.add(node);
            } else if (ss[1].equals("1") && maxQ.size() != 0) {
                while (maxQ.size() != 0 && set.contains(maxQ.peek().id)) {
                    maxQ.poll();
                }
                if (maxQ.size() != 0) {
                    set.add(maxQ.poll().id);
                }
            } else if (ss[1].equals("-1") && minQ.size() != 0) {
                while (minQ.size() != 0 && set.contains(minQ.peek().id)) {
                    minQ.poll();
                }
                if (minQ.size() != 0) {
                    set.add(minQ.poll().id);
                }
            }
        }

        int[] answer = { 0, 0 };

        while (maxQ.size() != 0 && set.contains(maxQ.peek().id)) {
            maxQ.poll();
        }
        if (maxQ.size() != 0) {
            answer[0] = -maxQ.peek().val;
        }

        while (minQ.size() != 0 && set.contains(minQ.peek().id)) {
            minQ.poll();
        }
        if (minQ.size() != 0) {
            answer[1] = minQ.peek().val;
        }

        return answer;
    }

}
