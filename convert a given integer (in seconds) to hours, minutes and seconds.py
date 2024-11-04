import java.util.Scanner;

public class ConvertSeconds {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        
        int totalSeconds = sc.nextInt();

        int hours = totalSeconds / 3600; 
        int minutes = (totalSeconds % 3600) / 60; 
        int seconds = totalSeconds % 60; 
        System.out.println("H:"+"M:"+"S"+"-"+hours+":"+minutes+":"+seconds);

        sc.close(); 
    }
}