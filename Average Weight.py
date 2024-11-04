import java.util.Scanner;

public class AverageWeight {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        int W1 = scanner.nextInt();
        int W2 = scanner.nextInt();
        scanner.close();
        
        int totalWeight = X * 3;
        int W3 = totalWeight - W1 - W2;
        
        System.out.println(W3);
    }
}