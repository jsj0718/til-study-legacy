package str;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_10809 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] arr = new int[26];
		for(int i=0; i<arr.length; i++) {
			arr[i] = -1;
		}
		
		String str = br.readLine();
		br.close();

		for(int i=0; i<str.length(); i++) {
			if (arr[str.charAt(i) - 'a'] == -1 ) {
				arr[str.charAt(i) - 'a'] = i;
			}
		}
		
		for(int k : arr) {
			System.out.print(k + " ");
		}
	}
}
