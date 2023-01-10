class Solution {
    var ans = 0

    fun recur(n: Int, li: MutableList<Int>, bit: Int) {
        if (li.size == n) {
            ans++
            return
        }

        for (i in 1..n) {
            if (bit and (1 shl i) == 0) {
                if (i % (li.size + 1) == 0 || (li.size + 1) % i == 0) {
                    li.add(i)
                    recur(n, li, bit or (1 shl i))
                    li.removeAt(li.size - 1)
                }
            }
        }
    }

    fun countArrangement(n: Int): Int {
        recur(n, mutableListOf(), 0)
        return ans
    }
}
