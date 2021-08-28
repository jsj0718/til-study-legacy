package dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_1003 {
	// int 배열일 경우 -1로 선언, Integer 배열일 경우 null로 비교 가능 (더 간편)
	public static Integer[][] arr = new Integer[41][2];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		
		for (int i=0; i<T; i++) {
			// 0과 1일 때 각각 호출 횟수 초기화
			arr[0][0] = 1;
			arr[0][1] = 0;
			arr[1][0] = 0;
			arr[1][1] = 1;
			
			int n = Integer.parseInt(br.readLine());
			fibo(n);
			
			sb.append(arr[n][0]).append(" ").append(arr[n][1]).append("\n");
		}
		
		System.out.println(sb);
	}
	
	
	public static Integer[] fibo(int n) {
		// 0 또는 1 호출 횟수가 null인 경우 재귀 호출 (int 배열이면 -1로 초기화 후 비교)
		if (arr[n][0] == null || arr[n][1] == null) {
			arr[n][0] = fibo(n-1)[0] + fibo(n-2)[0];
			arr[n][1] = fibo(n-1)[1] + fibo(n-2)[1];
		}
		
		return arr[n];
	}
}
