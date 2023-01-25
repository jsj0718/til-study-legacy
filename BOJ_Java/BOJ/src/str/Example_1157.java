package str;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_1157 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine().toUpperCase();
		int[] arr = new int[26];

		for (int i=0; i<str.length(); i++) {
			arr[str.charAt(i) - 'A']++;
		}
		
		int max = -1;
		char ch = '?';
		for (int i=0; i<arr.length;i++) {
			if (max < arr[i]) {
				max = arr[i];
				ch = (char) ('A' + i);
			} else if (max == arr[i]){
				ch = '?';
			}
		}
		
		System.out.println(ch);
		
	}
}
