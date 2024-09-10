import java.util.Scanner;
public class Excercise1{
public static void main(String... args){
	
	Scanner scanner = new Scanner(System.in);
	
	int sumPass = 0;
	int sumFail = 0;
	
	System.out.print("Enter a number between 1 and 2: ");
	int number = scanner.nextInt();
	
	if (number != 1 && number != 2) sumFail += 1;
	else sumPass += 1;
	
	while (number != 1 && number != 2){
	System.out.print("Enter a number between 1 and 2: ");
	 number = scanner.nextInt();
	 
	if (number != 1 && number != 2) sumFail += 1;
	else sumPass += 1;
	   
	}
	System.out.printf("Total number of passes = %d", sumPass);
	System.out.printf("Total number of failures = %d", sumFail);
	
	
	
	
	
}
	
	
	
	
	
}