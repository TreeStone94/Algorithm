import java.util.*;

public class Main{
    public static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        int a  = scan.nextInt();
        int b  = scan.nextInt();
        int c  = scan.nextInt();

        System.out.println((a+b)%c);
        System.out.println(((a%c)+(b%c))%c);
        System.out.println((a*b)%c);
        System.out.println(((a%c) * (b%c))%c);

    }
}