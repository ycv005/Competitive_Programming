import java.util.ArrayList;
import java.util.Scanner;

class FindAnyIndex {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split("\\s+");
        ArrayList<Integer> a = new ArrayList<Integer>();
        for (int i = 0; i < line.length; i++) {
            a.add(Integer.parseInt(line[i]));
        }
        int k = sc.nextInt();
        System.out.println(printAnyIndex(a, k, 0));
        sc.close();
    }

    public static int printAnyIndex(ArrayList<Integer> a, int k, int i) {
        if (i >= a.size()) {
            return -1;
        } else if (a.get(i) == k) {
            return i;
        }
        return printAnyIndex(a, k, ++i);
    }
}