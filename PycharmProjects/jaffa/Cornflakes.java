import java.util.Scanner;
public class Cornflakes{
public static void main(String...args){

	Scanner scanner = new Scanner;
	System.out.print("Enter a number: ");
	int userInput = scanner.nextInt(); 
	int result = 0;

	for (int number = 1; number <= 10; number++){
		result = userInput * number 
		System.out.printf("%d x %d = %d", userInput, number, result);
		}



	}
}