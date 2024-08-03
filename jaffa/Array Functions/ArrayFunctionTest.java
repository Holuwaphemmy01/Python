import static org.junit.Assert.*;
import java.util.Arrays;
import org.junit.jupiter.api.Test;

public class ArrayFunctionTest{ 

@Test
public void testForLargestNumberInAList(){

	//given
	ArrayFunctions arrayfunctions = new ArrayFunctions();
	//when
	int [] large = {7, 56, 86, 45, 67, 34, 89, 987, 67, 34, 654};
	int result = arrayfunctions.largestElement(large); 
	//assert
	assertEquals(987, result);
		}

@Test
public void testForReverseNumberInAList(){

	//given
	ArrayFunctions arrayfunctions = new ArrayFunctions();
	//when
	int [] reverse = {6, 8, 9, 10};
	int [] newReverse = {10, 9, 8, 6};
	
	
	//assert
	assertArrayEquals(newReverse, arrayfunctions.reverseElement(reverse));
		}


@Test
public void testToLookForNumberInAList(){

	//given
	ArrayFunctions arrayFunctions = new ArrayFunctions();
	//when
	int [] odd = {45, 34, 23, 12, 45, 34, 62, 41, 78, 56};
	int [] newOdd = {0, 34, 0, 12, 0, 34, 0, 41, 0, 56};
	//assert
	assertArrayEquals(newOdd, arrayFunctions.oddPosition(odd));

			}


@Test
public void testToLookForNumberEvenInAList(){

	//given
	ArrayFunctions arrayFunctions = new ArrayFunctions();
	//when
	int [] even = {34, 56, 23, 78, 56, 34, 89, 90, 45};
	int [] result = {34, 0, 23, 0, 56, 0, 89, 0, 45};
	//assert
	assertArrayEquals(result, arrayFunctions.evenPosition(even));

			}

  
@Test
public void testForTotalElementInTheList(){

		//given
	ArrayFunctions arrayFunctions = new ArrayFunctions();
		//when
	int [] even = {56, 57, 23, 45, 21, 83, 35, 89};
	int result = 410;
		//assert
	assertEquals(result, arrayFunctions.totalOfAllList(even));

			}

@Test
public void testForStringPalindrome(){

		//given
	ArrayFunctions arrayFunctions = new ArrayFunctions();
		//when
	String word = "oluwafemiytut";
	boolean result = arrayFunctions. checkForPalindrome(word);
	
		//assert
	assertEquals(false, result);
			}


@Test
public void testForTotalSumUsingWhileLoop(){

	ArrayFunctions arrayFunctions = new ArrayFunctions();
	int [] addition = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	int result = 55;
	assertEquals(result, arrayFunctions.sumOfNumbersUsingWhileLoop(addition)); 	

			}

/*@Test
public void testForTotalSumOfArrayUsingDoWhileLoop(){

	ArrayFunctions arrayFunctions = new ArrayFunctions();
	int [] addition = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	int result = 55;
	assertEquals(result, arrayFunctions.sumofArrayUsingDoWhileLoop(addition));

				}**/






	}