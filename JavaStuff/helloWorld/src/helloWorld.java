import java.util.Scanner;

public class helloWorld {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Type someting");

        String newString = sc.nextLine();
        System.out.println(newString);
        sc.close();
    }
}
