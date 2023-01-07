class Solution {
    fun maxIceCream(costs: IntArray, coins: Int): Int {
        costs.sort()
        var cur = coins
        for (i in costs.indices) {
            if (costs[i] > cur) return i
            else cur -= costs[i]
        }
        return costs.size
    }
}
