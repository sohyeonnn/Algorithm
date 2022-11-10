/*
1. 0번째 숫자는 무조건 answer list에 추가해준다.
2. 만약 현재 list의 값이 그 전의 값과 다르다면 answer list에 추가, 같다면 추가하지 않음
*/
import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> arrList = new ArrayList<Integer>();
        
        for(int i=0; i<arr.length; i++){
            
            if(i==0){
                arrList.add(arr[i]);
            }
            
            else if(arr[i] != arr[i-1]){
                arrList.add(arr[i]);
            }
            
        }
        //answer 리스트 크기 선언후 Integer ArrayList을 int 배열로 변환
        answer = new int[arrList.size()];
        for (int i = 0 ; i < arrList.size() ; i++) {
            answer[i] = arrList.get(i).intValue();
        }
        return answer;
    }
}
