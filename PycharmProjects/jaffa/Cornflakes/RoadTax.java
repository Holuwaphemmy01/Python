import java.util.Scanner;
public class RoadTax{
public static void main(String...args){

	Scanner scanner = new Scanner(System.in);
	double roadtax = 0;

	System.out.print("Enter the price of your car: ");
	double price = scanner.nextDouble();

	if (price <= 1000000){
		roadtax = price * 0.10;
		System.out.print(roadtax);
		}
	else if (price >= 1000000 && price < 3000000){
		roadtax = price * 0.15;
		System.out.print(roadtax);
		}
	else if (price >= 3_000_000 && price < 5_000_000){
		roadtax = price * 0.20;
		System.out.print(roadtax);
		}
	else
		roadtax = price * 0.25;
		System.out.print(roadtax);
	}


}