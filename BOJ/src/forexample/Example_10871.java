package forexample;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Example_10871 {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] str = bf.readLine().split(" ");
		int T = Integer.parseInt(str[0]);
		int X = Integer.parseInt(str[1]);
		
		String[] array = bf.readLine().split(" ");
		for (int i=0; i<T; i++) {
			if (Integer.parseInt(array[i]) < X) {
				bw.write(array[i] + " ");
			}
		}
		bf.close();
		
		bw.flush();
		bw.close();
		
	}
}
