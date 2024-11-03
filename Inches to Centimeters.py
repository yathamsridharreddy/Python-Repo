import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

public class InchesToCentimeters {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the height in inches
        int heightInInches = scanner.nextInt();
        
        // Convert height to centimeters (1 inch = 2.54 centimeters)
        double heightInCentimeters = heightInInches * 2.54;
        
        // Round the result to 2 decimal places
        BigDecimal roundedHeight = new BigDecimal(heightInCentimeters).setScale(2, RoundingMode.HALF_UP);
        
        // Print the height in centimeters
        System.out.println(roundedHeight);
        
        scanner.close();
    }
}