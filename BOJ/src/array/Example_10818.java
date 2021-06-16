package array;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Example_10818 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int minVal = 1000001;
		int maxVal = -1000001;
		
		while(st.hasMoreTokens()) {
			int val = Integer.parseInt(st.nextToken());
			if (minVal > val) {
				minVal = val;
			}
			
			if (maxVal < val) {
				maxVal = val;
			}
		}
		
		br.close();
		
		bw.write(minVal + " " + maxVal);
		bw.flush();
		bw.close();
		
		/* 다른 풀이 방법	
		 	int maxVal = 0;
			int index = 0;
			for(int i=0; i<9; i++) {
				int val = Integer.parseInt(br.readLine());
				if (maxVal < val) {
					maxVal = val;
					index = i + 1;
				}
			}
		 */
	}

}
