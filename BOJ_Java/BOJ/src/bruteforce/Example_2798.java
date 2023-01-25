package bruteforce;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_2798 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
		int T = Integer.parseInt(st1.nextToken());
		int M = Integer.parseInt(st1.nextToken());
		
		StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
		int[] arr = new int[T];
		for (int i=0; i<T; i++) {
			arr[i] = Integer.parseInt(st2.nextToken());
		}
		int result = 0;
		
		for (int i=0; i<T-2; i++) {
			for(int j=i+1; j<T-1; j++) {
				for(int k=j+1; k<T; k++) {
					int value = arr[i] + arr[j] + arr[k];
					if (result < value && M >= value) {
						result = arr[i] + arr[j] + arr[k];
					}
				}
			}
		}
		
		System.out.println(result);
	}

}
