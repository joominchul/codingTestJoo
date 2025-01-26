class Solution {
    fun solution(s1: Array<String>, s2: Array<String>): Int {
        var answer: Int = 0
        s1.forEach{
            if(s2.contains(it)){
                answer += 1
            }
        }
        return answer
    }
}
//https://school.programmers.co.kr/learn/courses/30/lessons/120903
