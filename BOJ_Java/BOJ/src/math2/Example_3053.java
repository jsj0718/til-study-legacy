package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_3053 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int r = Integer.parseInt(br.readLine());
		
		double result1 = Math.PI * r * r;
		double result2 = 2 * r * r;
		
		System.out.println(result1);
		System.out.println(result2);
		
	}
}
