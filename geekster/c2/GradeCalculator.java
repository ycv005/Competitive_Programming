import java.util.Scanner;

public class GradeCalculator {
    public static void main(String[] args) {
        System.out.println("Enter all 3 marks to get the average= ");
        Scanner sc = new Scanner(System.in);
        System.out.print("First mark- ");
        int a = sc.nextInt();
        System.out.print("Second mark- ");
        int b = sc.nextInt();
        System.out.print("Third mark- ");
        int c = sc.nextInt();
        // while (scanner.hasNext()) {
        // System.out.println(scanner.nextInt());
        // }
        int val = (int) ((a + b + c) / 3);
        if (90 <= val && val <= 100) {
            System.out.println("A");
        } else if (80 <= val && val <= 89) {
            System.out.println("B");
        } else if (60 <= val && val <= 79) {
            System.out.println("C");
        } else if (60 <= val && val <= 69) {
            System.out.println("D");
        } else if (0 <= val && val <= 59) {
            System.out.println("E");
        } else {
            System.out.println("Wrong input provided");
        }
        sc.close();
    }
}
