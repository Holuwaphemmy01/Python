import java.util.Scanner;
public class Bank{
public static void main(String... args){

	Scanner input = new Scanner(System.in);

	int accountbalance = 0;
	int userInput = 0;
	int deposit = 0;
	int withdraw = 0;
	
	while(userInput != 4){
	String message = """
			    1. Deposit
			    2. Withdraw
			    3. Check balance
			    4. To end   """;
	System.out.print(message);
	System.out.println();
	System.out.print("Enter a number above to continue: ");
	userInput = input.nextInt();

	if (userInput == 1){
		System.out.print("Enter amount to deposit: ");
		deposit = input.nextInt();
	accountbalance += deposit;
	System.out.println();
	}

	else if (userInput == 2){
		System.out.print("Enter amount to withdraw: ");
		withdraw = input.nextInt();
		if (withdraw > accountbalance){
			System.out.print("invalid amount");
			}
		else if (withdraw < 0){
			System.out.print("invalid amount");
		}
		else 
		accountbalance -= withdraw;
	System.out.println();
			}

	else if (userInput == 3){
		System.out.print(accountbalance);
		System.out.println();
		}
	else if (userInput == 4){
			break;
			}
	else 
		break;
		}
	
	

}


}