import java.util.Scanner;
public class ArithmeticOperations
{
    public static void main(String args[])
    {
      Scanner sc=new Scanner(System.in);
      int a=sc.nextInt();
      int b=sc.nextInt();
      int s=a+b;
      int d=a-b;
      int p=a*b;
      int q=a/b;
      int r=a%b;
      System.out.println("Sum:"+s);
      System.out.println("Difference:"+d);
      System.out.println("Product:"+p);
      System.out.println("Quotient:"+q);
      System.out.println("Remainder:"+r);  
    }
}