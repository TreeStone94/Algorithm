import java.util.*;

public class Main{
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {

        int a =scan.nextInt();
        int b = scan.nextInt();

        System.out.println(a * (b%10));
        System.out.println(a * (b%100 / 10));
        System.out.println(a * (b%1000 / 100));
        System.out.println(a*b);


    }
}

