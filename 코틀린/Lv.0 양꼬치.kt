//https://school.programmers.co.kr/learn/courses/30/lessons/120830
class Solution {
    fun solution(n: Int, k: Int): Int {
        var answer: Int = n * 12000 + (k - n / 10) * 2000
        return answer
    }
}
