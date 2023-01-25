package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_11653_T {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder();
		for (int i=2; i*i<=N; i++) {
			// N이 소수가 아닌 경우
			while (N % i == 0) {
				sb.append(i).append("\n");
				N /= i;
			}
		}
		
		// N이 소수인 경우
		if (N != 1) {
			sb.append(N).append("\n");
		}
		
		System.out.println(sb);
	}
}
