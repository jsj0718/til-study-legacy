package recursion;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_10870 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		System.out.println(fibo(T));
	}
	
	static int fibo(int a) {
		if (a < 2) {
			return a;
		}
		return fibo(a-1) + fibo(a-2); 
	}
}
