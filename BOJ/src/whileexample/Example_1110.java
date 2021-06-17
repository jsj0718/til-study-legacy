package whileexample;

import java.util.Scanner;

public class Example_1110 {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int result = num;
		int count = 0;
		
		do {
			result = (result % 10) * 10 + ((result / 10) + (result % 10)) % 10;
			count++;
		} while (result != num);
		
		System.out.println(count);
	}
}
