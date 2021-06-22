package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_1929 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[N-M+1];
		
		for (int i=M, idx=0; i<=N; idx++, i++) {
			arr[idx] = i;
		}
		
		for (int k : arr) {
			if (prime(k)) {
				System.out.println(k);
			}
		}
	}
	
	static boolean prime(int number) { 
		if (number == 1) {
			return false;
		}
		for (int i=2; i*i<=number; i++) {
			if (number % i == 0) {
				return false;
			}
		}
		return true;
	}
}
