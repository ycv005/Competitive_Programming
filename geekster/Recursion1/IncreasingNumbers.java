import java.util.Scanner;

public class IncreasingNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        printIncreasingNumbers(1, n);
        sc.close();
    }

    public static void printIncreasingNumbers(int a, int n) {
        if (n <= 0) {
            return;
        }
        System.out.println(a);
        printIncreasingNumbers(++a, --n);
    }
}
