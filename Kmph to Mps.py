import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

public class KmphToMps {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the speed in kilometers per hour
        int speedKmph = scanner.nextInt();
        
        // Convert speed to meters per second
        double speedMps = speedKmph * 1000.0 / 3600.0;
        
        // Round the result to 2 decimal places
        BigDecimal roundedSpeed = new BigDecimal(speedMps).setScale(2, RoundingMode.HALF_UP);
        
        // Print the speed in meters per second
        System.out.println(roundedSpeed);
        
        scanner.close();
    }
}