package array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_2577 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int val = Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine());
		String str = String.valueOf(val);
		int[] array = new int[10];
		
		br.close();
		
		for (int i=0; i<str.length(); i++) {
			int idx = str.charAt(i) - '0';
			array[idx]++;
		}
		
		for (int k : array) {
			System.out.println(k);
		}

	}
}
