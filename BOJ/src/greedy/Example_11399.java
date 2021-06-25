package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Example_11399 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		ArrayList<Integer> list = new ArrayList<>();
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i=0; i<T; i++) {
			list.add(Integer.parseInt(st.nextToken()));
		}
		
		list.sort(null);
		
		int result = 0;
		for (int i=0; i<T; i++) {
			for (int j=0; j<i+1; j++) {
				result += list.get(j);
			}
		}
		
		System.out.println(result);
	}
}
