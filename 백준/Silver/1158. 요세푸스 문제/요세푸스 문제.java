import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		//now = 현재 인덱스 값을 저장할 변수
		//size는 최대 인덱스 값을 저장할 변수
		int now = K;
		int size = N;
		
		List<Integer> list1 = new ArrayList<Integer>();
		List<Integer> list2 = new ArrayList<Integer>();
		
		for(int i = 1; i <= N; i++) {
			list1.add(i);
		}
		
		//해당 인덱스 값을 list1에서 list2로 이동해주고, list1에서는 제거해준다.
		for(int i = 0; i < N; i++) {
			list2.add(list1.get(now - 1));
			list1.remove(now - 1);
			now += (K - 1);
			size--;
			
			if(size != 0) {
				//최댓값보다 현재 값이 커지면, 현재값이 최댓값보다 작아질때까지 최댓값을 빼준다.
				//계속 빼주는 이유는 최댓값은 점점 작아지고, 현재값에 추가되는 값은 같기때문에
				//최댓값이 작아질수록 빼줘야하는 횟수가 늘어날 것이다.
				while(now > size) {
					now -= size;
				}
			}
		}
		//출력.
		System.out.print("<");
		for(int i = 0; i < N; i++) {
			if(i == (N - 1)) System.out.print(list2.get(i) + ">");
			else System.out.print(list2.get(i) + ", ");
		}
	}

}