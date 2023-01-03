class Node(val url: String) {
    var prev: Node? = null
    var next: Node? = null
}

class BrowserHistory(homepage: String) {
    var cur = Node(homepage)

    fun visit(url: String) {
        cur.next = Node(url)
        cur.next!!.prev = cur
        cur = cur.next!!
    }

    fun back(steps: Int): String {
        var cnt = steps
        while (cnt-- > 0 && cur.prev != null) {
            cur = cur.prev!!
        }

        return cur.url
    }

    fun forward(steps: Int): String {
        var cnt = steps
        while (cnt-- > 0 && cur.next != null) {
            cur = cur.next!!
        }

        return cur.url
    }

}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
