import java.util.*;

public class PrimeNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number= ");
        int n = sc.nextInt();
        if (n < 0) {
            System.out.println("Enter a positive val");
        } else {
            if (n <= 2) {
                System.out.println("Prime");
            } else {
                int i = 2;
                boolean isPrime = true;
                while (i <= (int) Math.sqrt(n)) {
                    if (n % ++i == 0) {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime) {
                    System.out.println("Prime");
                } else {
                    System.out.println("Not Prime");
                }
            }
        }
        sc.close();
    }
}
