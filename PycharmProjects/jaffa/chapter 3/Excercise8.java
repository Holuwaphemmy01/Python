import java.util.Scanner;
public class Excercise8{
public static void main(String...args){

	Scanner scanner = new Scanner(System.in);
	
	int sum = 0;
	int product = 1;
	int number1 = 0;
	int number2 = 0;
	int number3 = 0;
	int userInput = 0;
	
	
	for (int number = 1; number <= 3; number++){
		System.out.print("Enter number: ");
		 userInput = scanner.nextInt();
		
	if (userInput > largest)
		largest = userInput;
	if (userInput < largest)
		smallest = userInput; 		

			sum *= userInput;

	}
		
	System.out.println(largest);
	System.out.println(smallest);
	}

}