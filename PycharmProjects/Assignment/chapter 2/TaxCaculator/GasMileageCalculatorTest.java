import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class GasMileageCalculatorTest{ 

	
	@Test
	public void testCanCanCaculateMilePerGallon(){

		//given
		GasMileageCalculator calculator = new GasMileageCalculator();
	
		//when
		double numberOfMilesDriven = 30.00;
		double numberOfGallonsUsed = 20;
		double milesPerGallon = calculator. computeMilesPerGallon(numberOfMilesDriven, numberOfGallonsUsed);


		//assert
		 assertEquals(1.5, milesPerGallon);

			}












}