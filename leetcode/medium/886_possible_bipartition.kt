class Solution {
    fun recur(cur: Int, graph: Array<MutableSet<Int>>, color: Array<Int>): Boolean {
        for (next in graph[cur]) {
            if (color[cur] == color[next]) return true
            if (color[next] != -1) continue
            
            color[next] = (color[cur] + 1) % 2
            if (recur(next, graph, color)) return true
        }

        return false
    }

    fun possibleBipartition(n: Int, dislikes: Array<IntArray>): Boolean {
        val graph = Array(n + 1) { mutableSetOf<Int>() }

        for (arr in dislikes) {
            graph[arr[0]].add(arr[1])
            graph[arr[1]].add(arr[0])
        }

        val color = Array(n + 1) { -1 }

        for (i in 0..n) {
            if (color[i] != -1) continue
            color[i] = 0
            if (recur(i, graph, color)) return false
        }

        return true
    }
}
