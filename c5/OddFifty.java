public class OddFifty {
	public static void main(String[] args) {
		int arr[] = new int[10];
		
		for(int i = 0, num = 51; i < 10; i++, num += 2) {
			arr[i] = num;
			System.out.println(num);
		}
	}
}