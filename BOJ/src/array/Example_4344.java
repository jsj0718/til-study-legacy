package array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_4344 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		int[] arr;
		StringTokenizer st;
		for (int i=0; i<T; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			arr = new int[Integer.parseInt(st.nextToken())];
			double sum = 0.0;
			
			for (int j=0; j<arr.length; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
				sum += arr[j];
			}
			
			double avg = sum / arr.length;
			double cnt = 0.0;
			
			for (int k : arr) {
				if (k > avg) {
					cnt++;
				}
			}
			
			System.out.printf("%.3f%%\n", (cnt / arr.length) * 100);
			
		}
		
		br.close();
	}
}
