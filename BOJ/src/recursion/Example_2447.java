package recursion;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_2447 {
	public static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				stars(N/3, i, j);
			}
			sb.append("\n");
		}
		
		System.out.println(sb);

	}

	public static void stars(int N, int i, int j) {
		if (i%3 == 1 && j%3 == 1) {
			sb.append(" ");
			return;
		}

		if (N == 1) {
			sb.append("*");
			return;
		}
		stars(N/3, i/3, j/3);
	}

}
