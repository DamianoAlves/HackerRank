package if_else;
import java.util.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        scanner.close();

        System.out.println(weirdTest(N));
    }

    public static String weirdTest(int value){
        if(value % 2 != 0 ){
            return "Weird";
        } else if(value >= 2 && value <=5 ){
            return "Not Weird";
        } else if(value >= 6 && value <=20){
            return "Weird";
        } else{
            return "Not Weird";
        }
    }
}