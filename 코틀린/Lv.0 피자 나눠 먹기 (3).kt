class Solution {
    fun solution(slice: Int, n: Int): Int {
        var answer: Int = n / slice
        if(n > answer * slice){
            answer += 1
        }
        return answer
    }
}
//https://school.programmers.co.kr/learn/courses/30/lessons/120816
