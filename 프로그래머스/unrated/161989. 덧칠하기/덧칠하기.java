class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        
        int size = section.length;  //section 길이
        int next = section[0];  //지나갈 다음자리
        int index = 0;  //section index
        
        while(index < size) {
            if(next <= section[index]) {
                next = section[index] + m;
                    answer ++;
            }
            index++;
        }
        
        return answer;
    }
}