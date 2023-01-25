package str;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_1316_1 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		int result = 0;
		
		for (int i=0; i<T; i++) {		
			String str = br.readLine();
			boolean[] arr = new boolean[26];	// 그룹 단어 체크용 boolean 배열 선언
			for (int k=0; k<str.length(); k++) {
				if (arr[str.charAt(k) - 'a'] == true) {	// 이미 나온 적이 있으면 break
					break;					
				}
				
				if (k < str.length()-1 && str.charAt(k) != str.charAt(k+1)) {	//	다음 문자와 비교하여 다르면 true 전환
					arr[str.charAt(k) - 'a'] = true;
				} 
				
				if (k == str.length()-1) {	// k가 마지막까지 도달하면 result++
					result++;
				}
			}
			
		}
		
		System.out.println(result);
		
		
	}
}
