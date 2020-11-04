import java.util.ArrayList;
import java.util.Scanner;

public class MinimumInArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> a = new ArrayList<Integer>();
        String[] line = sc.nextLine().split("\\s+");
        for (int i = 0; i < line.length; i++) {
            a.add(Integer.parseInt(line[i]));
        }
        System.out.println(getminimumInArray(a, 0, Integer.MAX_VALUE));
        sc.close();
    }

    public static int getminimumInArray(ArrayList<Integer> a, int index, int min) {
        if (index == a.size() - 1) {
            return min;
        }
        min = Math.min(a.get(index), min);
        return getminimumInArray(a, index + 1, min);
    }
}
