import java.util.Scanner;

public class RomeoAndJuliet {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        int Y = scanner.nextInt();
        int Z = scanner.nextInt();
        scanner.close();
        
        int totalMoney = (5 * X) + (10 * Y);
        int maxChocolates = totalMoney / Z;

        System.out.println(maxChocolates);
    }
}