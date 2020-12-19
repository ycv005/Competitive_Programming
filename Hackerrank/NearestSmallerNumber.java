import java.io.*;
import java.util.*;

public class NearestSmallerNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // String s = br.readLine();
        int n = Integer.parseInt(br.readLine());
        // String[] line = br.readLine().split(" ");
        int[] input = Arrays.stream(br.readLine().split("\\s+")).mapToInt(Integer::parseInt).toArray();
        Stack<Integer> st = new Stack<>();
        String ans = "";
        for (int i = 0; i < input.length; i++) {
            int v = input[i];
            ans += Integer.toString(nearSmaller(input, i));
            // if (st.empty()) {
            // ans += "-1";
            // st.push(v);
            // } else {
            // if (st.peek() < v) {
            // ans += Integer.toString(st.peek());
            // st.push(v);
            // } else {
            // while (!st.empty() && st.peek() >= v) {
            // st.pop();
            // }
            // if (st.empty()) {
            // ans += "-1";
            // } else {
            // ans += Integer.toString(st.peek());
            // }

            // }
            // }
            ans += " ";
        }
        System.out.println(ans);
    }

    private static int nearSmaller(int[] arr, int j) {
        int tmp = arr[j];
        for (int i = j - 1; i >= 0; i--) {
            if (arr[i] < tmp) {
                return arr[i];
            }
        }

        return -1;
    }
}
