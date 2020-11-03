import java.util.Scanner;

class Fibonacci {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        getFibonacci(n, 0, 1);
        System.out.println();
        sc.close();
    }

    public static void getFibonacci(int n, int l1, int l2) {
        if (n <= 0) {
            return;
        }
        if (l1 != 0) {
            System.out.print(" ");
        }
        System.out.print(l1);
        n--;
        getFibonacci(n, l2, l1 + l2);
    }
}