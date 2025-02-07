//https://school.programmers.co.kr/learn/courses/30/lessons/87390?language=kotlin
class Solution {
    fun solution(n: Int, left: Long, right: Long): IntArray {
        val answer = IntArray((right - left + 1).toInt())
        var index = 0
        for (count in left..right) {
            val row = (count / n).toInt()
            val col = (count % n).toInt()
            answer[index++] = maxOf(row, col) + 1
        }
        return answer
    }
}
