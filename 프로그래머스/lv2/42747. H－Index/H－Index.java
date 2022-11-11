/*
h의 최대값이 H-Index의 값이다.
h가 x일때의 개수 -> 배열 정렬
*/
import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        Arrays.sort(citations);
        
        for(int i=0; i<citations.length; i++){
            int h = citations.length - i;   //해당 논문보다 인용 횟수가 크거나 같은 논문의 편수
            
            if(citations[i] >= h){    //H-Index 조건
                answer = h;     //조건에 만족하면
                break;      //탈출해서 answer 반환
            }
        }
        return answer;
    }
}