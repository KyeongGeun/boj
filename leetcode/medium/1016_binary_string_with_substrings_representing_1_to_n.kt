class Solution {
    fun queryString(s: String, n: Int): Boolean {
        val set = mutableSetOf<Int>()
        for (i in s.indices) {
            val sb = StringBuilder()
            for (j in i until s.length) {
                sb.append(s[j])
                try {
                    set.add(sb.toString().toInt(2))
                } catch (e : Exception) {
                    break
                }
            }
        }

        for (i in 1..n)
            if (i !in set)
                return false
        return true
    }
}
