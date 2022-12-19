class Solution {
    fun shiftingLetters(s: String, shifts: IntArray): String {
        shifts[shifts.size - 1] %= 26
        for (i in shifts.size - 2 downTo 0) {
            shifts[i] = (shifts[i] + shifts[i + 1]) % 26
        }

        return s.mapIndexed { idx, c -> (c - 97 + shifts[idx]).toInt() % 26 + 97 }
            .map { it.toChar() }
            .joinToString("")
    }
}
