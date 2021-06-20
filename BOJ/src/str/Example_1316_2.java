package str;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_1316_2 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		
		int T = Integer.parseInt(br.readLine());
		int result = 0;
		
		for (int i=0; i<T; i++) {		
			if (check()) {
				result++;
			}
		}
		
		System.out.println(result);	
		
	}
	
	public static boolean check() throws IOException {
		
		String str = br.readLine();
		boolean[] check = new boolean[26];
		int prev = 0;
		
		for (int i=0; i<str.length(); i++) {
			char now = str.charAt(i);
			
			if (prev != now) {
				if (!check[now - 'a']) {
					check[now - 'a'] = true;
					prev = now;
				} else {
					return false;
				}
			}
		}
		return true;
	}
}
