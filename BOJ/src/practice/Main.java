package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] array = new int[42];
		
		for (int i=0; i<10; i++) {
			int val = Integer.parseInt(br.readLine());
			if (array[val%42] == 0) {
				array[val%42]++;
			}
		}
		br.close();
		
		int result = 0;
		for (int i=0; i<array.length; i++) {
			result += array[i];
		}
		
		System.out.println(result);
	}

}
