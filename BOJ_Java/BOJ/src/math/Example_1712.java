package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_1712 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int roomNum = Integer.parseInt(br.readLine());
		
		int cnt = 0;
		int n = 0;
		while (true) {
			cnt++;
			if ((6*(n) + 1) < roomNum) {
				n += cnt;
			} else {
				break;
			}
		}
		
		System.out.println(cnt);
	}
}
