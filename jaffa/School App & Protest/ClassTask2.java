import java.util.Arrays;
public class ClassTask2{


public static int[] ascendingOrder(int [] array){
		

	for(int index = 0; index < array.length; index++){
			for(int element = index + 1; element < array.length; element++){
				if(array[index] > array[element]){
		 			 array[index] = array[index] + array[element];
					 array[element] = array[index] - array[element];
					 array[index] = array[index] - array[element];
					
										}
									}
					} 
				return array;

				}


	public static void main(String[] args){
	int [] array = {10, -4, 5, 2, -6, 80, 0};
	int[] arraySorts = ascendingOrder(array);
	System.out.print(Arrays.toString(array));


}



	}





 





			



	