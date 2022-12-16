import java.util.Arrays;
import java.util.Comparator;

class Solution {
    int[] parent;

    public int find(int x) {
        if (parent[x] < 0) return x;

        parent[x] = find(parent[x]);
        return parent[x];
    }

    public boolean union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return false;

        if (parent[x] > parent[y]) {
            int temp = x;
            x = y;
            y = temp;
        }

        parent[x] += parent[y];
        parent[y] = x;

        return true;
    }

    public int solution(int n, int[][] costs) {

        parent = new int[n];
        Arrays.fill(parent, -1);

        Arrays.sort(costs, Comparator.comparing(cost -> cost[2]));

        int ans = 0;
        int cnt = 0;
        for (int[] cost : costs) {
            if (union(cost[0], cost[1])) {
                ans += cost[2];
                cnt++;

                if (cnt == n - 1) return ans;
            }
        }

        return ans;
    }
}