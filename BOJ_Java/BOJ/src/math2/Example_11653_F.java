package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_11653_F {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int i = 2;
		StringBuilder sb = new StringBuilder();
		
		while (N != 1) {
			if (!prime(i)) {
				i++;
			} else {
				if (N % i == 0) {
					sb.append(i).append("\n");
					N = N / i;
				} else {
					i++;
				}
			}
		}
		
		System.out.println(sb);
	}
	
	static boolean prime(int a) {
		if (a == 1) {
			return false;
		}
		for(int i=2;i*i<=a;i++) {
			if (a % i == 0) {
				return false;
			}
		}
		return true;
	}
}
