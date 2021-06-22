package math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_10757 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		String num1 = st.nextToken();
		String num2 = st.nextToken();
		
		int maxLength = Math.max(num1.length(), num2.length());
		int[] numA = new int[maxLength+1];
		int[] numB = new int[maxLength+1];
		
		for(int i=num1.length()-1, idx=0; i>=0; idx++, i--) {
			numA[idx] = num1.charAt(i) - '0';
		}
		
		for(int i=num2.length()-1, idx=0; i>=0; idx++, i--) {
			numB[idx] = num2.charAt(i) - '0';
		}
		
		for(int i=0; i<maxLength; i++) {
			int value = numA[i] + numB[i];
			numA[i] = value % 10;
			numA[i+1] += (value / 10);
		}
		
		StringBuilder sb = new StringBuilder();
		
		if (numA[maxLength] != 0) {
			sb.append(numA[maxLength]);
		}
		
		for (int i=maxLength-1; i>=0; i--) {
			sb.append(numA[i]);
		}
		
		System.out.println(sb);
	}
}
