import java.util.*

class Solution {
    fun minStoneSum(piles: IntArray, k: Int): Int {
        val pq = PriorityQueue<Int> { o1, o2 -> o2 - o1 }

        pq.addAll(piles.toList())

        var n = k
        while (n --> 0) {
            pq.add((pq.poll() + 1) / 2)
        }

        return pq.sum()
    }
}
