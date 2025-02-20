import java.util.*;

public class Main{
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {

        int a =scan.nextInt();
        String b =scan.next();
        int increaseIndex = 10;
        int y= 0;
        for(int i=b.length()-1; i>=0;i--) {
            int x = a* Integer.parseInt(String.valueOf(b.charAt(i)));
            System.out.println(x);
            if(i == b.length()-1) {
                y += x;
            } else {
                y += (x * increaseIndex);
                increaseIndex *= increaseIndex;
            }
        }

        System.out.println(y);


    }
}

