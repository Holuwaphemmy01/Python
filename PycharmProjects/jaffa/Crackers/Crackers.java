import java.lang.Math;
import java.util.Arrays;
public class Crackers{

public double myDiscount(double price, double discount){

		double result = (price / 100) * discount;
	double results = price - result;
		return results;
		}



public double divideOrSquare(double number){
	double result = 0;
	if(number % 5 == 0){
	     result = Math.sqrt(number);
		}
	else {
		result = number % 5;
		}
	return result;
		}



public boolean equalStrings(String stringOne, String stringTwo){
	if (stringOne.length() != stringTwo.length()){
			return false;
	}
	
	char[] charArrayOne = stringOne.toCharArray();
	char[] charArrayTwo = stringTwo.toCharArray();
	Arrays.sort(charArrayOne);
	Arrays.sort(charArrayTwo);
	return Arrays.equals(charArrayOne, charArrayTwo);
		}
/*public static void main(String...args){

System.out.println(equalStrings("love", "olve"));
System.out.println(equalStrings("love", "live"));

		}**/

}