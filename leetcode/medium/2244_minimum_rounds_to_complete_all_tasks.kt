class Solution {
    fun minimumRounds(tasks: IntArray): Int {
        val map = mutableMapOf<Int, Int>()
        for (task in tasks) {
            map[task] = map.getOrDefault(task, 0) + 1
        }

        var ans = 0
        for (v in map.values) {
            var cur = v
            while (cur > 0) {
                if (cur < 2) return -1
                if (cur % 3 == 0) {
                    ans += cur / 3
                    break
                }
                cur -= 2
                ans += 1
            }
        }

        return ans
    }
}
