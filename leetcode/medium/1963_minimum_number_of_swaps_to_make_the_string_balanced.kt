class Solution {
    fun minSwaps(s: String): Int {
        var l = 0
        var ans = 0
        for (c in s) {
            if (c == '[') l++
            else if (l > 0) l--
            else {
                l++
                ans++
            }
        }
        return ans
    }
}
