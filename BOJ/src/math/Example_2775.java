package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_2775 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		for (int i=0; i<T; i++) {
			int[][] arr = new int[15][15];
			int a = Integer.parseInt(br.readLine());
			int b = Integer.parseInt(br.readLine());
			
			for (int x=0; x<=a; x++) {
				int sum = 0;
				for (int y=0; y<=b; y++) {
					if (x == 0) {
						arr[x][y] = y;
					} else {
						sum += arr[x-1][y];
						arr[x][y] = sum;
					}
				}
			}
			sb.append(arr[a][b]).append("\n");
		}
		
		System.out.println(sb);
	}
}
