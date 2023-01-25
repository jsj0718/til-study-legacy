package backtracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Example_2580 {
	public static int[][] arr = new int[9][9];
	public static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		for (int i=0; i<9; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j=0; j<9; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		sudoku(0, 0);
	}
	
	public static void sudoku(int row, int col) {
		// col이 9가 되면 row를 1 증가시키고, col은 0으로 초기화
		if (col == 9) {
			sudoku(row+1, 0);
			return;
		}
		
		// row가 9가 되면 최종 arr를 출력시키고 시스템 종료
		if (row == 9) {
			for (int[] a : arr) {
				for (int num : a) {
					sb.append(num).append(" ");
				}
				sb.append("\n");
			}
			System.out.println(sb);
			// return은 상위 sudoku 함수로 되돌아감 (이 때 return을 통해 마지막 탐색까지 진행했을 때 다 채워진다는 보장 X)
			// 따라서 해당 열과 행이 모두 채워지면 바로 시스템을 종료시킴
			System.exit(0);
		}
		
		// 빈 값인 경우 백트래킹을 통해 값 탐색
		if (arr[row][col] == 0) {
			for (int i=1;i<=9;i++) {
				if (possible(row, col, i)) {
					arr[row][col] = i;
					sudoku(row, col+1);
				}
			}
			// 1~9까지 모두 되지 않는다면 return (해당 경로는 틀린 경로로 다른 경로를 탐색하도록 유도)
			arr[row][col] = 0;
			return;
		}
		
		// 빈 값이 아닌 경우 다음 값 탐색 진행
		sudoku(row, col+1);
	}
	
	public static boolean possible(int row, int col, int val) {
		// 같은 열에 같은 값이 있는 경우
		for (int i=0; i<9; i++) {
			if (arr[i][col] == val) {
				return false;
			}
		}

		// 같은 행에 같은 값이 있는 경우
		for (int j=0; j<9; j++) {
			if (arr[row][j] == val) {
				return false;
			}
		}
		
		// 같은 상자에 같은 값이 있는 경우
		for (int i=row/3*3; i<row/3*3+3; i++) {
			for (int j=col/3*3; j<col/3*3+3; j++) {
				if (arr[i][j] == val) {
					return false;			
				}
			}
		}
		return true;
	}
}


//테스트케이스 #1
//0 3 5 4 6 9 2 7 8
//7 8 2 1 0 5 6 0 9
//0 6 0 2 7 8 1 3 5
//3 2 1 0 4 6 8 9 7
//8 0 4 9 1 3 5 0 6
//5 9 6 8 2 0 4 1 3
//9 1 7 6 5 2 0 8 0
//6 0 3 7 0 1 9 5 2
//2 5 8 3 9 4 7 6 0

//테스트케이스 #2
//0 0 0 0 0 0 0 0 0
//0 0 0 0 0 0 0 0 0
//0 0 0 0 0 0 0 0 0
//0 0 0 0 0 0 0 0 0
//0 0 0 0 0 0 0 0 0
//0 0 0 0 0 0 0 0 0
//0 0 0 0 0 0 0 0 0
//0 0 0 0 0 0 0 0 0
//0 0 0 0 0 0 0 0 0

//테스트케이스 #3
//0 2 0 9 0 5 0 0 0
//5 9 0 0 3 0 2 0 0
//7 0 0 6 0 2 0 0 5
//0 0 9 3 5 0 4 6 0
//0 5 4 0 0 0 7 8 0
//0 8 3 0 2 7 5 0 0
//8 0 0 2 0 9 0 0 4
//0 0 5 0 4 0 0 2 6
//0 0 0 5 0 3 0 7 0