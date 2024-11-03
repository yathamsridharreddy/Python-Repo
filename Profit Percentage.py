import java.util.Scanner;

public class ProfitPercentage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read cost price (CP) and selling price (SP)
        double cp = scanner.nextDouble();
        double sp = scanner.nextDouble();
        
        // Calculate profit percentage
        double profitPercentage = ((sp - cp) / cp) * 100;
        
        // Print result formatted to 2 decimal places
        System.out.printf("%.2f", profitPercentage);
        
        scanner.close();
    }
}