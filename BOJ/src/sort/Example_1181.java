package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Example_1181 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String[] arr = new String[N];
		
		for (int i=0; i<N; i++) {
			arr[i] = br.readLine();
		}
		
		// Comparator를 통해 이중 정렬 진행(길이 -> 사전순)
		Arrays.sort(arr, new Comparator<String>() {
			@Override
			public int compare(String s1, String s2) {
				if (s1.length() == s2.length()) {
					return s1.compareTo(s2);
				} else {
					return s1.length() - s2.length();
				}
			}
		});
		
		// 중복 단어 제거 (equals() 사용)
		StringBuilder sb = new StringBuilder();
		sb.append(arr[0]).append("\n");
		for (int i=1; i<N; i++) {
			if (arr[i].equals(arr[i-1])) {
				continue;
			} else {
				sb.append(arr[i]).append("\n");
			}
		}
		System.out.println(sb);
	}
}
