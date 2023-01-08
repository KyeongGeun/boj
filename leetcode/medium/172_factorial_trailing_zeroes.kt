class Solution {
    fun trailingZeroes(n: Int): Int {
        var ans = 0
        var cur = n
        while (cur > 0) {
            ans += cur / 5
            cur /= 5
        }
        return ans
    }
}
