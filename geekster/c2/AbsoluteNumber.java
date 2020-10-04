import java.util.Scanner;

class AbsoluteNumber {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the number, to get its absolute value= ");
        int num = in.nextInt();
        if (num < 0) {
            num *= -1;
        }
        System.out.println("result= " + num);
        in.close();
    }
}