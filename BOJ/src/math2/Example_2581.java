package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_2581 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		
		int[] arr = new int[N-M+1];
		
		for(int i=M, idx=0; i<=N; i++, idx++) {
			arr[idx] = i;
		}
		
		int sum = 0;
		int min = 10001;
		for(int k : arr) {
			if (prime(k)) {
				sum += k;
				if (min > k) {
					min = k;
				}
			}
		}
		
		if (sum == 0) {
			System.out.println(-1);
		} else {
			System.out.println(sum);
			System.out.println(min);
		}
	}
	
	static boolean prime(int number) {
		if (number == 1) {
			return false;
		}
		for(int j=2; j*j<=number; j++) {
			if (number % j == 0) {
				return false;
			}
		}
		return true;
	}
}
