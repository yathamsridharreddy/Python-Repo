import java.util.Scanner;

public class DaysToYearsWeeks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int D = scanner.nextInt();
        scanner.close();
        
        int years = D / 365;
        int remainingDays = D % 365;
        int weeks = remainingDays / 7;

        System.out.println(years);
        System.out.println(weeks);
    }
}