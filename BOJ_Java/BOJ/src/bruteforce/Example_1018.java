package bruteforce;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_1018 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer stInt = new StringTokenizer(br.readLine());
		
		int row = Integer.parseInt(stInt.nextToken());
		int col = Integer.parseInt(stInt.nextToken());			
		Boolean[][] blist = new Boolean[row][col];
		
		for (int i=0; i<row; i++) {
			String boardLine = br.readLine();
			for (int j=0; j<col; j++) {
				if (boardLine.charAt(j) == 'W') {
					blist[i][j] = true;					
				} else {
					blist[i][j] = false;
				}
			}
		}
		
		int min = 2501;
		for (int i=0; i<=row-8; i++) {
			for (int j=0; j<=col-8; j++) {
				int val = chess(blist, i, j);
				if (min > val) {
					min = val;
				}
			}
		}
		
		System.out.println(min);
		
	}

	public static int chess(Boolean[][] blist, int x, int y) {
		int result = 0;
		Boolean bool = blist[x][y];
		for (int i=x; i<x+8; i++) {
			for (int j=y; j<y+8; j++) {
				if (blist[i][j] != bool) {
					result++;
				}
				bool = !bool;
			}
			bool = !bool;
		}
		
		
		return Math.min(result, 64 - result);
	}
}
