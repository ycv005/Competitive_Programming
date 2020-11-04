import java.util.ArrayList;
import java.util.Scanner;

public class ReverseArray {
    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<Integer>();
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split("\\s+");
        for (int i = 0; i < line.length; i++) {
            a.add(Integer.parseInt(line[i]));
        }
        reverseArray(a, 0);
        sc.close();
    }

    private static void reverseArray(ArrayList<Integer> a, int i) {
        if (i >= a.size()) {
            return;
        }
        reverseArray(a, i + 1);
        if (i == 0) {
            System.out.println(a.get(i));
        } else {
            System.out.print(a.get(i) + " ");
        }
    }
}
