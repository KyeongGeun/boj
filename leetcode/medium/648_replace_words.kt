class Solution {
    fun replaceWords(dictionary: List<String>, sentence: String): String {
        val set = dictionary.toSet()
        val words = sentence.split(" ").toMutableList()

        for (i in words.indices) {
            var word = words[i]
            val sb = StringBuilder()
            for (j in word.indices) {
                sb.append(word[j])
                if (sb.toString() in set) break
            }
            words[i] = sb.toString()
        }

        return words.joinToString(" ")
    }
}
