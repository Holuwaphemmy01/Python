import java.util .Arrays;
public class ArrayFunctions{


public static int largestElement(int[]large){
	int largest = large[0];
	
	for(int number = 1; number < large.length; number++){
		if (large[number] > largest){
		largest = large [number];
		}
			}
	return largest;
	
		}
		

		

public static int[] reverseElement(int[]reverse){
	int [] newReverse = new int [reverse.length];
	int count = 0;
	for(int index = reverse.length-1;  index >=  0; index--){
		newReverse[count] = reverse[index];
		count++; 
				}
			return newReverse;
			
				}

public static int[] oddPosition(int[]odd){
			int length = odd.length;
			int [] newOdd = new int [length];
		for(int index = 0, odds = 0; index < odd.length; index++, odds++){
			 if (index % 2 != 0){
				newOdd[odds] = odd[index]; 
				
					}						
					}
			return newOdd;

			}





public static int [] evenPosition(int [] even){

	int [] newEven = new int [even.length];
	
   for(int index = 0; index < even.length; index++){
		if (index % 2 == 0) newEven[index] = even[index];

				}

		return newEven;
	
				}


public static int totalOfAllList(int [] total){

	int result = 1;
	for (int index = 0; index < total.length; index++){

			result += total[index];

				}

		return result;

			}

	/*public static void main(String[] args){
	int [] array = {10, 4, 5, 2, 6, 80, 0};
	int result = totalOfAllList(array);
	System.out.print(result);

			}**/

public static boolean checkForPalindrome(String word){
int lengths = word.length();

	for(int index = 0; index < lengths/2; index++){

		if (word.charAt(index)==(word.charAt(lengths-1-index))){
			return true;
					}
			
				
					}
			return false;
					}
public static int sumOfNumbersUsingWhileLoop(int [] number){ 
		int index = 0;
		int sum = 0;
		while (index < number.length){
			sum += number[index];
				index++;
					}
			return sum;
			  	
				}

public static int sumofArrayUsingDoWhileLoop(int [] number){
			int index = 0;
			int sum = 0;
			do{
				sum += number[index];
				}
			while(index < number.length);
			return sum;
			}


	} 