import java.util.Scanner;

public class VolumeOfSphere {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the radius of the sphere
        double radius = scanner.nextDouble();
        
        // Calculate the volume of the sphere
        double volume = (4.0 / 3.0) * 3.14 * Math.pow(radius, 3);
        
        // Print the result formatted to 2 decimal places
        System.out.printf("%.2f", volume);
        
        scanner.close();
    }
}