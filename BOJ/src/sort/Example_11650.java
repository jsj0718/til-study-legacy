package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Example_11650 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N][2];
		
		for(int i=0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = Integer.parseInt(st.nextToken());
		}
		
		// 2차원 배열 정렬 방법(Comparator 사용)
		Arrays.sort(arr, new Comparator<int[]>() {
			@Override
			public int compare(int[] t1, int[] t2) {
				if (t1[0] == t2[0]) {
					return t1[1] - t2[1];
				} else {
					return t1[0] - t2[0];
				}
			}
		});
		
		StringBuilder sb = new StringBuilder();
		for (int i=0; i<N; i++) {
			sb.append(arr[i][0] + " " + arr[i][1]).append("\n");
		}
		
		System.out.println(sb);
	}
}
