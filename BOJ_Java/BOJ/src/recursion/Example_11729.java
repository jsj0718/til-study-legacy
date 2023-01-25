package recursion;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_11729 {
	// System.out.println()은 시간초과가 발생하여 StringBuilder로 대체
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		sb.append((int) Math.pow(2, N) - 1).append("\n");
		hanoi(N, 1, 2, 3);
		
		System.out.println(sb);
	}
	
	static void hanoi(int N, int start, int via, int to) {
		if (N == 1) {
			sb.append(start + " " + to).append("\n");
			return;
		}
		
		// step 1
		hanoi(N-1, start, to, via);
		
		// step 2
		sb.append(start + " " + to).append("\n");
		
		// step 3
		hanoi(N-1, via, start, to);
	}
}
