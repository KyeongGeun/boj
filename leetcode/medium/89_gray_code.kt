class Solution {
    private val list = mutableListOf(0)
    val set = mutableSetOf(0)

    val check = {
        val bit = list.first() and list.last()
        bit and (bit - 1) == 0
    }

    fun recur(n: Int): Boolean {
        if (list.size == (1 shl n)) return check()

        for (i in 0..n) {
            val last = list.last()
            val bit = last xor (1 shl i)
            if (bit in set) continue

            list.add(bit)
            set.add(bit)
            if (recur(n)) return true
            list.remove(list.size - 1)
            set.remove(bit)
        }

        return false
    }

    fun grayCode(n: Int): List<Int> {
        recur(n)
        return list
    }
}
