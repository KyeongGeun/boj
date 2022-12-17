class Solution {
    fun integerBreak(n: Int): Int {
        if (n == 2) return 1
        if (n == 3) return 2

        var ans = 1
        var cur = n
        while (cur > 4) {
            ans *= 3
            cur -= 3
        }

        return ans * cur
    }
}
