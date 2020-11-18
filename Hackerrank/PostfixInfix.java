import java.util.*;

class PostfixInfix {

    public static boolean isOperator(Character c) {
        int val = (int) c;
        if ((65 <= val && val <= 90) || (97 <= val && val <= 122)) {
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        Stack<String> st = new Stack<String>();
        st.push(s.charAt(0) + "");
        for (int i = 1; i < s.length(); i++) {
            if (isOperator(s.charAt(i))) {
                String second = st.pop();
                String first = st.pop();
                st.push("(" + first + s.charAt(i) + second + ")");
            } else {
                st.push(s.charAt(i) + "");
            }
        }
        System.out.println(st.peek());
        scanner.close();
    }
}