class Solution {

    val ans = mutableListOf<List<Int>>()
    val visited = mutableSetOf<Int>()

    fun recur(cur: Int, list: MutableList<Int>, graph: Array<IntArray>) {
        if (cur == graph.size - 1) ans.add(list.toList())
        for (num in graph[cur]) {
            if (num in visited) continue
            list.add(num)
            visited.add(num)
            recur(num, list, graph)
            list.removeAt(list.size - 1)
            visited.remove(num)
        }
    }

    fun allPathsSourceTarget(graph: Array<IntArray>): List<List<Int>> {
        visited.add(0)
        recur(0, mutableListOf(0), graph)

        return ans
    }
    
}
