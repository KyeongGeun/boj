class Solution {
    fun canCompleteCircuit(gas: IntArray, cost: IntArray): Int {
        if (gas.sum() - cost.sum() < 0) return -1

        var cur = 0
        var ans = 0
        for (i in gas.indices) {
            cur += gas[i] - cost[i]

            if (cur < 0) {
                cur = 0
                ans = i + 1
            }
        }

        return ans
    }
}
