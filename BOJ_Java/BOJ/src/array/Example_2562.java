package array;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Example_2562 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int maxVal = 0;
		ArrayList<Integer> array = new ArrayList<>();
		
		
		for(int i=0; i<9; i++) {
			int val = Integer.parseInt(br.readLine());
			array.add(val);
			if (maxVal < val) {
				maxVal = val;
			}
		}
		
		br.close();
		
		bw.write(maxVal + "\n" + (array.indexOf(maxVal)+1));
		bw.flush();
		bw.close();
	}
}
