import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CrackersTest{

@Test
public void discountForMyProduct(){
		//given
		Crackers crackers = new Crackers();
		//when
		double results = crackers.myDiscount(150, 15);
		//assert
		assertEquals(127.5, results);
			}

@Test
public void numbersThatCanDivideOrSquare(){

		//given
		Crackers crackers = new Crackers();
		//when
		double result = crackers.divideOrSquare(27);
		//assert
		assertEquals(2, result);

		}
@Test
public void compareTwoString(){

		//given
		Crackers crackers = new Crackers();
		//when
		boolean result = crackers.equalStrings("love", "loev");
		//assert
		assertTrue(result);

		}








}