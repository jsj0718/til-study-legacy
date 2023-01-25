package backtracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_15650 {
	public static int[] arr;
	public static boolean[] visited;
	public static StringBuilder sb = new StringBuilder();
		
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		visited = new boolean[N];
		arr = new int[M];
		
		dfs(N, M, 0);
		System.out.println(sb);
	}
	
	
	public static void dfs(int N, int M, int depth) {
		if (M == depth) {
			for (int val : arr) {
				sb.append(val).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i=0; i<N; i++) {
			// 오름차순이 아니라면 넘어가기
			if (depth != 0 && arr[depth-1] >= (i + 1)) {
				continue;
			}
			if (!visited[i]) {
				visited[i] = true;
				arr[depth] = i + 1;
				dfs(N, M, depth+1);
				visited[i] = false;
			}
		}
	}
}
