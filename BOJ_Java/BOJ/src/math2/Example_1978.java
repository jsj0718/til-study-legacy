package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_1978 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int[] arr = new int[T];
		
		// 배열 초기화
		for (int i=0; i<T; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int cnt = 0;
		for (int k : arr) {
			if (prime(k)) {
				cnt++;
			}
		}
		
		System.out.println(cnt);
	}
	
	// 소수 판별 메소드 선언
	static boolean prime(int number) {
		if (number == 1) {
			return false;
		}
		for(int j=2; j*j<=number; j++) {
			if (number % j == 0) {
				return false;
			}
		}
		return true;
	}
}
