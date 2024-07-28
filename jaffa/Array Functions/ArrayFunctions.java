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
		

		

public static int[]reverseElement(int[]reverse){
	int [] newReverse = new int [reverse.length];
	for(int count = 0, index = 0;  index < reverse.length; index++, count++){
		newReverse[count] = reverse[reverse.length - index];
				}
			return newReverse;
			
				}

/*public static int oddPosition(int[]odd){
		for(int index = 0 ; index <= odd.length-1; index++){
			 if (odd[index] % 2 != 0){
				return odd{index};

					}						
						}


			}**/




	


	}