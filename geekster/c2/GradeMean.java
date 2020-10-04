import java.util.Scanner;

public class GradeMean {
    public static void main(String[] args) {
        System.out.println("Enter a Correct grade between A to F");
        Scanner sc = new Scanner(System.in);
        char txt = sc.next().charAt(0);
        if (txt == 'A') {
            System.out.println("Excellent");
        } else if (txt == 'B') {
            System.out.println("Good");
        } else if (txt == 'C') {
            System.out.println("Average");
        } else if (txt == 'D') {
            System.out.println("Deficient");
        } else if (txt == 'E') {
            System.out.println("Failing");
        } else {
            System.out.println("Wrong input provided");
        }
        sc.close();
    }
}
