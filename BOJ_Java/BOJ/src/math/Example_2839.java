package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_2839 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int result = 0;
		
		if (N == 4 || N == 7) {
			result = -1;
		} else if (N % 5 == 0) {
			result = N / 5;
		} else if (N % 5 == 1 || N % 5 == 3) {
			result = N / 5 + 1;
		} else if (N % 5 == 2) {
			result = (N / 5) + (N % 5);
		} else {
			result = ((N + 1) / 5) + 1;
		}
		
		System.out.println(result);
	}
}
