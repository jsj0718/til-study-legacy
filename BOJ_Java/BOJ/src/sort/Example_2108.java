package sort;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Example_2108 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		ArrayList<Integer> list = new ArrayList<>();
		
		int sum = 0;
		for (int i=0; i<N; i++) {
			list.add(Integer.parseInt(br.readLine()));
			sum += list.get(i);
		}
		
		Collections.sort(list);
		
		int avg = (int) Math.round((double) sum / N);
		int median = list.get(N/2);
		int mode;
		int range = list.get(N-1) - list.get(0);
		
		System.out.println(avg);
		System.out.println(median);
		System.out.println(range);
	}
}
