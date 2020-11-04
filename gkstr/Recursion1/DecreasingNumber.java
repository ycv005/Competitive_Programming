import java.util.Scanner;

/**
 * DecreasingNumber
 */
public class DecreasingNumber {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        decAndPrint(n);
        sc.close();
    }

    public static void decAndPrint(int n) {
        System.out.println(n--);
        if (n > 0) {
            decAndPrint(n);
        }
    }
}