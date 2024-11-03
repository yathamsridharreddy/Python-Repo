import java.util.Scanner;

public class DiskCapacity {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the number of tracks (T), sectors (S), and blocks (B)
        int T = scanner.nextInt();
        int S = scanner.nextInt();
        int B = scanner.nextInt();
        
        // Each block has 512 bytes
        int bytesPerBlock = 512;

        // Calculate total capacity in bytes
        long totalCapacityInBytes = T * S * B * bytesPerBlock;

        // Convert bytes to kilobytes (1 KB = 1024 bytes)
        long totalCapacityInKB = totalCapacityInBytes / 1024;

        // Print the capacity in KB
        System.out.println(2*totalCapacityInKB + " KB");
        
        scanner.close();
    }
}