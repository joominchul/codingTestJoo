//https://school.programmers.co.kr/learn/courses/30/lessons/120817
class Solution {
    fun solution(numbers: IntArray): Double {
        var answer: Double = 0.0
        for(num in numbers){
            answer += num * 1.0
        }
        return answer / numbers.size
    }
}
