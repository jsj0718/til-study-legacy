package array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_8958 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		int[] arr = new int[T];
		
		for (int i=0; i<T; i++) {
			String str = br.readLine();
			int cnt = 0;
			int score = 0;
			for (int k=0; k<str.length(); k++) {
				if (str.charAt(k) == 'O') {
					cnt++;
				} else {
					cnt = 0;
				}
				score += cnt;
			}
			arr[i] = score;
		}
		
		for (int i : arr) {
			System.out.println(i);
		}
	}
}
