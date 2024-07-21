import java.util.Scanner;
public class MortgageCalculator{
public static void main(String...args){
	
	Scanner scanner = new Scanner(System.in);
	
	int principalAmount = 0;
	int years = 0;
	int annualInterestRate = 0 / 100;
	int monthlyPayment = 0;
	
	
	System.out.print("Enter Amount to borrowed: ");
	principalAmount = scanner.nextInt();

	System.out.print("Enter number of years to payback: ");
	years = scanner.nextInt();
	
	System.out.print("Enter annual interest Rate: ");
	annualInterestRate = scanner.nextInt();
	
	int firstStep = annualInterestRate * (1 + annualInterestRate) * years;
	int secondStep = ((1 + annualInterestRate) * years) - 1;
	monthlyPayment = principalAmount * (firstStep / secondStep);
	
	System.out.print(monthlyPayment);
	
	
}
	
	
	
	
}