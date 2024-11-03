import java.util.Scanner;

public class LossPercentage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read cost price (CP) and selling price (SP)
        double cp = scanner.nextDouble();
        double sp = scanner.nextDouble();
        
        // Calculate loss percentage
        double lossPercentage = ((cp - sp) / cp) * 100;
        
        // Print result formatted to 2 decimal places
        System.out.printf("%.2f", lossPercentage);
        
        scanner.close();
    }
}