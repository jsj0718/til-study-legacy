package str;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Example_2941 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		
		String[] arr = {"dz=", "d-", "c=", "c-", "lj", "nj", "s=", "z="};

		for (int i=0; i<arr.length; i++) {
			str = str.replace(arr[i], "1");
		}
		
		System.out.println(str.length());
	}
}
