package backtracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_9663 {
	public static int N;
	public static int[] arr;
	public static int count = 0;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		arr = new int[N];
		nQueen(0);
		System.out.println(count);
	}
	
	public static void nQueen(int depth) {
		// 모든 퀸이 놓이면 count 증가
		if (depth == N) {
			count++;
			return;
		}
		
		for (int i=0; i < N; i++) {
			arr[depth] = i;
			if (possible(arr, depth)) {
				nQueen(depth+1);
			}
		}
	}
	
	public static boolean possible(int[] arr, int depth) {
		// 첫 행이라면 바로 true 반환
		if (depth == 0) {
			return true;
		}
		
		for (int i=0; i<depth; i++) {
			// 일직선 상에 있는 경우
			if (arr[depth] == arr[i]) {
				return false;
			}
			
			// 대각선에 있는 경우
			if (Math.abs(arr[depth] - arr[i]) == Math.abs(depth - i)) {
				return false;
			}
		}
		
		return true;
	}
}
