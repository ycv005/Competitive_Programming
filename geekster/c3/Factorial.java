import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number= ");
        int n = sc.nextInt();
        if (n < 0) {
            System.out.println("Enter a positive val");
        } else if (n <= 1) {
            System.out.println("Result: " + 1);
        } else {
            long v = 1;
            while (n >= 1) {
                v *= n;
                n -= 1;
            }
            System.out.println("Result: " + v);
        }
        sc.close();
    }
}
