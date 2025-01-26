//https://school.programmers.co.kr/learn/courses/30/lessons/120829
class Solution {
    fun solution(angle: Int): Int {
        var answer: Int = 0
        when{
            angle< 90 -> answer = 1
            angle== 90 -> answer = 2
            angle< 180 -> answer = 3
            else -> answer = 4
        }
        return answer
    }
}
