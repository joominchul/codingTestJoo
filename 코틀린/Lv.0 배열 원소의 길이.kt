class Solution {
    fun solution(strlist: Array<String>): IntArray {
        var answer: IntArray = IntArray(strlist.size)
        for(i in strlist.indices){
            answer.set(i, strlist[i].length)
        }
        return answer
    }
}
//https://school.programmers.co.kr/learn/courses/30/lessons/120854
