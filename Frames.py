import java.util.Scanner;

public class Frames {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int X = scanner.nextInt();
        scanner.close();
        
        int perimeter = 2 * (N + M);
        int cost = perimeter * X;
        
        System.out.println(cost);
    }
}