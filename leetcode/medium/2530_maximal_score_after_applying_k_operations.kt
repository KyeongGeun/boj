import java.util.*

class Solution {
    fun maxKelements(nums: IntArray, k: Int): Long {
        val pq = PriorityQueue<Int> { o1, o2 -> o2.compareTo(o1) }
        pq.addAll(nums.toList())

        var cnt = k
        var ans = 0L
        while (cnt-- > 0) {
            val max = pq.poll()
            ans += max
            pq.add((max + 2) / 3)
        }

        return ans
    }
}
