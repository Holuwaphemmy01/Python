import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ArrayFunctionTest{

@Test
public void testForLarestNumberInAList(){

	//given
	ArrayFunctions arrayfunctions = new ArrayFunctions();
	//when
	int [] large = {7, 56, 86, 45, 67, 34, 89, 987, 67, 34, 654};
	int result = arrayfunctions.largestElement(large); 
	//assert
	assertEquals(987, result);
		}

/*@Test
public void testForReverseNumberInAList(){

	//given
	ArrayFunctions arrayfunctions = new ArrayFunctions();
	//when
	int [] femi = {6, 8, 9, 10};
	int [] results = {10, 9, 8, 6};
	results = arrayfunctions.reverseElement(femi);
	
	//assert
	assertEquals(results, results);
		}**/

/*public void testforOddElements(){
		//given
		
		//when
		//assert


			}**/




	}