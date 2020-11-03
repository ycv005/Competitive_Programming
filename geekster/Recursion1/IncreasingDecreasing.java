import java.util.Scanner;

public class IncreasingDecreasing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        printIncreasingNumbers(1, n);
        decAndPrint(n);
        sc.close();
    }

    public static void decAndPrint(int n) {
        System.out.println(n--);
        if (n > 0) {
            decAndPrint(n);
        }
    }

    public static void printIncreasingNumbers(int a, int n) {
        if (n <= 0) {
            return;
        }
        System.out.println(a);
        printIncreasingNumbers(++a, --n);
    }
}
