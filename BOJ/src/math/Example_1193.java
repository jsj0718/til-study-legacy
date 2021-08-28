package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_1193 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(br.readLine());
		
		int row = 1;
		int col = 1;
		int cnt = 1;
		int val = 1;
		
		while (num != 0) {
			if (cnt == 1) {
				if (val % 2 == 0) {
					row = 1;
					col = val;
				} else {
					row = val;
					col = 1;
				}				
			} else {
				if (val % 2 == 0) {
					row++;
					col--;
				} else {
					row--;
					col++;
				}
			}
				
			if (cnt == val) {
				cnt = 1;
				val += 1;
			} else {
				cnt += 1;
			}
			
			num -= 1;
		}
		
		System.out.println(row + "/" + col);
	}

}
