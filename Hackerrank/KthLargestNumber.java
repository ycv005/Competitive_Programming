import java.util.*;
import java.io.*;

public class KthLargestNumber {
    public static void main(String[] args) throws IOException {
        // for min heap
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> mnHeap = new PriorityQueue<>(Collections.reverseOrder());
        String[] line = br.readLine().split(" ");
        int k = Integer.parseInt(line[1]);
        int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        for (int i = 0; i < input.length; i++) {
            mnHeap.add(input[i]);
        }
        for (int j = 0; j < k - 2; j++) {
            mnHeap.remove();
        }
        System.out.println(mnHeap.remove());
    }
}
