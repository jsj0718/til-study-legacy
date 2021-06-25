package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_3009 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] arr = new int[3][2];
		int a = 0;
		int b = 0;
		
		for(int i=0; i<arr.length; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			arr[i][0] = x;
			arr[i][1] = y;
		}
		
		
		if (arr[0][0] == arr[1][0]) {
			a = arr[2][0];
		} else if (arr[0][0] == arr[2][0]) {
			a = arr[1][0];
		} else {
			a = arr[0][0];
		}
		
		if (arr[0][1] == arr[1][1]) {
			b = arr[2][1];
		} else if (arr[0][1] == arr[2][1]) {
			b = arr[1][1];
		} else {
			b = arr[0][1];
		}
		
		System.out.println(a + " " + b);
	}
}
