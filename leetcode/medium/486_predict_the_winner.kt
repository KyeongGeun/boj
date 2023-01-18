class Solution {
    private val map = mutableMapOf<Int, Pair<Int, Int>>()

    private fun left(nums: IntArray, l: Int, r: Int, bit: Int): Pair<Int, Int> {
        if (l == r)
            return nums[l] to 0
        if (bit in map)
            return map[bit]!!

        val v1 = right(nums, l + 1, r, bit or (1 shl l))
        val v2 = right(nums, l, r - 1, bit or (1 shl r))

        val ans =
            if (v1.first + nums[l] > v2.first + nums[r])
                v1.copy(v1.first + nums[l])
            else
                v2.copy(v2.first + nums[r])

        map[bit] = ans
        return ans
    }

    private fun right(nums: IntArray, l: Int, r: Int, bit: Int): Pair<Int, Int> {
        if (l == r)
            return 0 to nums[l]
        if (bit in map)
            return map[bit]!!.second to map[bit]!!.first

        val v1 = left(nums, l + 1, r, bit or (1 shl l))
        val v2 = left(nums, l, r - 1, bit or (1 shl r))

        val ans =
            if (v1.second + nums[l] > v2.second + nums[r])
                v1.first to v1.second + nums[l]
            else
                v2.first to v2.second + nums[r]

        map[bit] = ans.second to ans.first
        return ans
    }

    fun PredictTheWinner(nums: IntArray): Boolean {
        val (l, r) = left(nums, 0, nums.size - 1, 0)
        return l >= r
    }
}
