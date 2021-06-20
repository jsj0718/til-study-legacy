package function;

public class Example_4673 {
	public static void main(String[] args) {
		boolean[] check = new boolean[10001];
		
		for (int i=1; i<10001; i++) {
			if (selfNumber(i) < 10001) {
				check[selfNumber(i)] = true;				
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int i=1; i<10001; i++) {
			if (!check[i]) {
				sb.append(i).append("\n");				
			}
		}
		
		System.out.println(sb);
	}
	
	public static int selfNumber(int number) {
		int sum = number;
		while (number != 0) {
			sum += number % 10;
			number /= 10;
		}
		return sum;
	}
}
