import java.util.ArrayList;
import java.util.Scanner;

public class LastOccurence {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> a = new ArrayList<Integer>();
        String[] line = sc.nextLine().split("\\s+");
        for (int i = 0; i < line.length; i++) {
            a.add(Integer.parseInt(line[i]));
        }
        int k = sc.nextInt();
        System.out.println(getLastIndex(a, k, a.size() - 1));
        sc.close();
    }

    public static int getLastIndex(ArrayList<Integer> a, int k, int l) {
        if (l < 0) {
            return -1;
        } else if (a.get(l) == k) {
            return l;
        }
        return getLastIndex(a, k, --l);
    }
}
