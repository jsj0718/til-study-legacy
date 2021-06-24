package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_9020 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int i=0; i<T; i++) {
			int n = Integer.parseInt(br.readLine());
			int a = 0;
			int b = 0;
			for (int j=2; j<=n/2; j++) {
				if (prime(j) && prime(n-j)) {
					a = j;
					b = n - j;
				}
			}
			sb.append(a + " " + b + "\n");
		}
		
		System.out.println(sb);
	}
	
	static boolean prime(int a) {
		if (a == 1) {
			return false;
		}
		
		for (int i=2; i*i<=a; i++) {
			if (a % i == 0) {
				return false;
			}
		}
		return true;
	}
}
