import java.lang.Math;
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
}