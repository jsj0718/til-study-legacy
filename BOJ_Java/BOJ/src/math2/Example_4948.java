package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_4948 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		while (true) {
			int N = Integer.parseInt(br.readLine());
			
			if (N == 0) {
				break;
			}
			
			int cnt = 0;
			for (int i=N+1; i<2*N+1; i++) {
				if (prime(i)) {
					cnt++;
				}
			}
			sb.append(cnt).append("\n");
		}
		
		System.out.println(sb);
		
	}
	
	static boolean prime(int number) {
		if (number == 1) {
			return false;
		}
		
		for (int i=2; i*i<=number; i++) {
			if (number % i == 0) {
				return false;
			}
		}
		return true;
	}
}
