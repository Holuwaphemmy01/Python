import java.util.Random;
import java.util.Scanner;
public class Generator{
public static void main(String...args){

	Scanner scanner = new Scanner(System.in);
	Random rand = new Random();
	System.out.print("Do you want to play game (Yes or No): ");
	String respond = scanner.nextLine();
	
		String userInput = null;
	
	if (respond.equals("Yes") || respond.equals ("yes")){

	int random = rand.nextInt(10);	
	while (respond != "No" || userInput != "no") {
	System.out.print("Guess a number from 1 to 10: ");
	int choice = scanner.nextInt();
	
	
	if (choice > random){
		System.out.println("Too High. Try again");
			}
	else if ( choice < random){
		System.out.println("Too low. Try again");
			}
	else if(choice == random){
		System.out.printf("Congratulations. You guessed the number%nDo you want to play again (Yes or no): ");
		respond = scanner.nextLine();
		
		
			}
	
	
	
	
	
	
			}
	
	
	
	
	
	
	
	}
	




}



}