import java.util.Scanner;

public class ValidTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("First degree- ");
        int a = sc.nextInt();
        System.out.print("Second degree- ");
        int b = sc.nextInt();
        System.out.print("Third degree- ");
        int c = sc.nextInt();
        if (a + b + c == 180) {
            System.out.println("Its a valid triangle");
        } else {
            System.out.println("Not a valid triangle");
        }
        sc.close();
    }
}
