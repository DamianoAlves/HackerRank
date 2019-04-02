import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        scan.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        int count = scan.nextInt();
        for (int i = 0; i< count; i++){
            String word = scan.next();
            System.out.println(getCharacters(word));
        }
    }

    public static String getCharacters (String word) {
        String even = new String();
        String odd = new String();
        for (int i = 0; i< word.length(); i++){
            if(i%2 == 0){
                even += word.charAt(i);
            } else {
                odd += word.charAt(i);
            }
        }
        even= even+" "+odd;
        return even;
    }

}