class Solution {
    fun asteroidCollision(asteroids: IntArray): IntArray {
        val li = mutableListOf<Int>()

        for (a in asteroids) {
            if (li.isEmpty() || li.last() < 0 || a > 0) {
                li.add(a)
                continue
            }

            while (li.isNotEmpty() && li.last() > 0 && li.last() < -a)
                li.removeAt(li.size - 1)

            if (li.isEmpty() || li.last() < 0)
                li.add(a)
            else if (li.last() == -a)
                li.removeAt(li.size - 1)
        }

        return li.toIntArray()
    }
}
