import java.util.Scanner;

public class Power {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        getPower(a, b, 1);
        sc.close();
    }

    public static void getPower(int a, int b, int c) {
        if (a == 1 || a == 0) {
            System.out.println(1);
            return;
        } else {
            if (b <= 0) {
                System.out.println(c);
                return;
            }
            getPower(a, --b, c * a);
        }
    }
}
