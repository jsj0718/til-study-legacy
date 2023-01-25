package recursion;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_10872 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		System.out.println(factorial(T));
	}
	
	static int factorial(int a) {
		if (a < 2) {
			return 1;
		}
		return a * factorial(a-1); 
	}
}
