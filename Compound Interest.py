import java.util.Scanner;

public class CompoundInterest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int P = scanner.nextInt();
        int R = scanner.nextInt();
        int T = scanner.nextInt();
        scanner.close();
        
        double amount = P * Math.pow(1 + (R / 100.0), T);
        double compoundInterest = amount - P;
        
        System.out.printf("%.2f", compoundInterest);
    }
}