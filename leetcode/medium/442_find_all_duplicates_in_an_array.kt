class Solution {
    fun findDuplicates(nums: IntArray): List<Int> {
        val set = mutableSetOf<Int>()
        val list = mutableListOf<Int>()

        nums.forEach { if (it in set) list.add(it) else set.add(it) }
        return list;
    }
}
