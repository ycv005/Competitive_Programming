import java.util.Scanner;

public class SumNNumer {
    public static void main(String[] args) {
        System.out.print("Enter a number= ");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        n = ((n + 1) * n) / 2;
        System.out.println("Result: " + n);
        sc.close();
    }
}
