package bruteforce;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_1436 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int cnt = 0;
		int i = 666;
		while (true) {
			if (check(i)) {
				cnt++;
			}
			if (cnt == N) {
				System.out.println(i);
				break;
			}
			i++;
		}
	}
	
	static boolean check(int a) {
		String str = a + "";
		return str.contains("666");
	}
}
