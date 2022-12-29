import java.util.*

class Solution {
    fun getOrder(tasks: Array<IntArray>): IntArray {
        val arr = tasks.mapIndexed { idx, arr -> intArrayOf(idx, *arr) }
            .sortedBy { arr -> arr[1] }

        val pq = PriorityQueue<IntArray>(compareBy({ it[2] }, { it[0] }))
        val ans = mutableListOf<Int>()
        var time = 0
        var i = 0
        while (i < tasks.size) {
            if (pq.size == 0 && time < arr[i][1]) time = arr[i][1]
            while (i < tasks.size && time >= arr[i][1]) pq.add(arr[i++])

            val poll = pq.poll()
            time += poll[2]
            ans.add(poll[0])
        }

        while (pq.isNotEmpty()) ans.add(pq.poll()[0])

        return ans.toIntArray()
    }
}
