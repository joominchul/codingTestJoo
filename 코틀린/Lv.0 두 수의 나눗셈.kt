//https://school.programmers.co.kr/learn/courses/30/lessons/120806
class Solution {
    fun solution(num1: Int, num2: Int): Int {
        var answer: Int = (num1.toDouble() / num2.toDouble() * 1000).toInt()
        return answer
    }
}
