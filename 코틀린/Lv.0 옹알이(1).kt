//https://school.programmers.co.kr/learn/courses/30/lessons/120956?language=kotlin
class Solution {
    fun solution(babbling: Array<String>): Int {
        var answer: Int = 0
        var stack = ""
        val two = listOf("ye", "ma")
        val three = listOf("aya", "woo")
        for(word in babbling){
            stack = ""
            for(i in word){
                stack += i
                if((stack.length == 2 && two.contains(stack)) || (stack.length == 3 && three.contains(stack))){
                    stack = ""
                }
            }
            if(stack.isEmpty()){
                answer += 1
            }
        }
        
        return answer
    }
}
