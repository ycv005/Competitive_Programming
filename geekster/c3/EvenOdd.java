import java.util.*;

class EvenOdd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> l1 = new ArrayList<Integer>();
        while (sc.hasNextInt()) {
            l1.add(sc.nextInt());
        }
        int even = 0, odd = 0;
        for (int i : l1) {
            if (i % 2 == 0) {
                even += i;
            } else {
                odd += i;
            }
        }
        System.out.println("Even- " + even);
        System.out.println("Odd- " + odd);
        sc.close();
    }
}