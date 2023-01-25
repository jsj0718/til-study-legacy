package str;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_2675 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());		
		for (int i=0; i<T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int r = Integer.parseInt(st.nextToken());
			String str = st.nextToken();
			for (int j=0; j<str.length(); j++) {
				for (int k=0; k<r; k++) {
					sb.append(str.charAt(j));					
				}
			}
			sb.append("\n");
		}
		
		br.close();
		
		System.out.println(sb);
	}
}
