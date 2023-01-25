package bruteforce;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_2231 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		for (int i=1; i<N+1; i++) {
			int result = sum(i);
			
			if (result == N) {
				System.out.println(i);
				break;
			}
			
			if (i == N) {
				System.out.println(0);
				break;
			}
			
		}	

	}		
	
	static int sum(int a) {
		int result = a;
		while (a != 0) {
			result += (a % 10);
			a /= 10;
		}
		return result;
	}
}
