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
			// N�� 5�� ����� �� cnt�� ���� ���ϰ� ���
			if (N % 5 == 0) {
				cnt += N / 5;
				System.out.println(cnt);
				break;
			}
			
			// �ƴ� ��� N�� -3�ϸ鼭 cnt++
			N -= 3;
			cnt++;
			
			// �� �� N�� 0���� ���� ���� 3, 5�� ����� �ƴϹǷ� -1 ���
			if (N < 0) {
				System.out.println(-1);
				break;
			}
		}
	}
}
