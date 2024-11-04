import java.util.Scanner;

public class LastTwoDigits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int year = scanner.nextInt();
        scanner.close();
        
        int lastTwoDigits = year % 100;

        System.out.printf("%02d", lastTwoDigits);
    }
}