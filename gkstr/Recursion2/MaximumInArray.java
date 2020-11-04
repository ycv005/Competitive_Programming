import java.util.ArrayList;
import java.util.Scanner;

public class MaximumInArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> a = new ArrayList<Integer>();
        String[] line = sc.nextLine().split("\\s+");
        for (int i = 0; i < line.length; i++) {
            a.add(Integer.parseInt(line[i]));
        }
        System.out.println(getMaximumInArray(a, 0, Integer.MIN_VALUE));
        sc.close();
    }

    public static int getMaximumInArray(ArrayList<Integer> a, int index, int max) {
        if (index == a.size() - 1) {
            return max;
        }
        max = Math.max(a.get(index), max);
        return getMaximumInArray(a, index + 1, max);
    }
}
