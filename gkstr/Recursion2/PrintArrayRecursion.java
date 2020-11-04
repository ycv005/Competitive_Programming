import java.util.ArrayList;
import java.util.Scanner;

public class PrintArrayRecursion {
    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<Integer>();
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split("\\s+");
        for (int i = 0; i < line.length; i++) {
            a.add(Integer.parseInt(line[i]));
        }
        printArrayRecursion(a, 0);
        sc.close();
    }

    private static void printArrayRecursion(ArrayList<Integer> a, int i) {
        if (i > a.size() - 1) {
            return;
        }
        System.out.print(a.get(i));
        if (i < a.size() - 1) {
            System.out.print(" ");
        } else {
            System.out.println();
        }
        printArrayRecursion(a, i + 1);
    }
}
