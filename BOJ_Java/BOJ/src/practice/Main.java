package practice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int roomNum = Integer.parseInt(br.readLine());
		
		int count = 1;
		int n1 = 0;
		int n2 = 0;
		while (true) {
			n2++;
			if ((6*(n1) + 1) < roomNum) {
				n1 += n2;
				count += 1;
			} else {
				break;
			}
		}
		
		System.out.println(count);
	}
	
}
