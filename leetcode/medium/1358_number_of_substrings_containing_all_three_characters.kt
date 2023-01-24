class Solution {
    fun check(arr: Array<Int>): Boolean {
        for (v in arr)
            if (v == 0)
                return false

        return true
    }

    fun numberOfSubstrings(s: String): Int {
        var ans = 0
        val cur = Array(3) { 0 }
        var l = 0
        var r = 0

        while (r < s.length) {
            cur[s[r] - 'a']++
            while (check(cur)) {
                cur[s[l] - 'a']--
                l++
                ans += s.length - r
            }
            r++
        }

        return ans
    }
}