package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_1712 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int fixedCost = Integer.parseInt(st.nextToken());
		int variableCost = Integer.parseInt(st.nextToken());
		int price = Integer.parseInt(st.nextToken());
		
		int result = 0;
		
		if (price > variableCost) {
			result = (fixedCost / (price - variableCost)) + 1;
		} else {
			result = -1;
		}
		
		System.out.println(result);
	}
}
