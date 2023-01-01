import kotlin.math.sqrt

class Solution {
    fun countPrimes(n: Int): Int {
        if (n < 3) return 0
        val primes = Array(n) { it % 2 != 0 }
        primes[0] = false
        primes[1] = false
        primes[2] = true

        for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
            if (primes[i])
                for (j in (i shl 1) until n step i)
                    primes[j] = false
        }

        return primes.filter { it }.size
    }
}
