package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Example_1427 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String N = br.readLine();
		int[] arr = new int[N.length()];
		
		for (int i=0; i<N.length(); i++) {
			arr[i] = N.charAt(i) - '0';
		}
		
		Arrays.sort(arr);
		
		StringBuilder sb = new StringBuilder();
		for (int i=arr.length-1; i>=0; i--) {
			sb.append(arr[i]);
		}
		
		System.out.println(sb);
	}
}
