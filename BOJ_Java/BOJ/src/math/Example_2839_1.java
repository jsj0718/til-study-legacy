package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_2839_1 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int cnt = 0;
		
		while (true) {
			// N이 5의 배수일 때 cnt에 몫을 더하고 출력
			if (N % 5 == 0) {
				cnt += N / 5;
				System.out.println(cnt);
				break;
			}
			
			// 아닌 경우 N에 -3하면서 cnt++
			N -= 3;
			cnt++;
			
			// 이 때 N이 0보다 작은 경우는 3, 5의 배수가 아니므로 -1 출력
			if (N < 0) {
				System.out.println(-1);
				break;
			}
		}
	}
}
