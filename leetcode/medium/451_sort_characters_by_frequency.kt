class Solution {
    fun frequencySort(s: String): String {
        val map = mutableMapOf<Char, Int>()
        for (c in s) {
            map[c] = map.getOrDefault(c, 0) + 1
        }

        val sb = StringBuilder()
        map.entries.sortedBy { -it.value }
            .forEach { sb.append(it.key.toString().repeat(it.value)) }

        return sb.toString()
    }
}
