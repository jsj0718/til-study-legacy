package math2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_1002 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int i=0; i<T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int r1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			int r2 = Integer.parseInt(st.nextToken());
			
			double realDist = Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2);
			
			// 완전 일치
			if (x1 == x2 && y1 == y2 && r1 == r2) {
				sb.append(-1).append("\n");
			// 내접 및 외접
			} else if (Math.pow((r1 + r2), 2) == realDist || Math.pow((r1 - r2), 2) == realDist) {
				sb.append(1).append("\n");
			} else if (Math.pow((r1 + r2), 2) < realDist || Math.pow((r1 - r2), 2) > realDist) {
				sb.append(0).append("\n");
			} else {
				sb.append(2).append("\n");
			}
		}
		
		System.out.println(sb);
	}
}
