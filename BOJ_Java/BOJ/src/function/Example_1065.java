package function;

import java.util.Scanner;

public class Example_1065 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.close();
		
		System.out.println(sequence(N));		
	}
	
	public static int sequence(int number) {
		int cnt = 0;
		
		// number가 100보다 작은 경우 모두 한수 
		if (number < 100) {
			cnt = number;
		// number가 100보다 큰 경우 등차 수열 계산 필요
		} else {
			cnt = 99;
			
			// 1000이 주어졌을 때 예외처리
			if (number == 1000) {
				number = 999;
			}
			
			// 등차 수열 계산
			for (int i=100; i<=number; i++) {
				int hun = i / 100;
				int ten = (i / 10) % 10;
				int one = i % 10;
				
				if ((hun - ten) == (ten - one)) {
					cnt++;
				}			
			}					
		}

		return cnt;
	}
}
