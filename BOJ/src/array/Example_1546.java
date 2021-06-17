package array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_1546 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		double[] array = new double[Integer.parseInt(br.readLine())];
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		double maxVal = -1000001;
				
		for (int i=0; i<array.length; i++) {
			array[i] = Double.parseDouble(st.nextToken());
			if (maxVal < array[i]) {
				maxVal = array[i];
			}
		}
		
		double sum = 0.0;
		for (double k : array) {
			sum += (k / maxVal) * 100;
		}
		
		double result = sum / array.length;
		System.out.println(result);
		
	}
}
