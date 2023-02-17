import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

import com.opencsv.CSVWriter;

public class App {

	final static int MAX_VALUE = 10000;

	public static void main(String[] args) {

		// (PART B) Generating array of increasing sizes
		int[][] InputArray = generateRandInput(MAX_VALUE);

		// Preparing Input Arrays
		int[][] InputArray_IS = InputArray.clone();
		int[][] InputArray_MS = InputArray.clone();
		int[][] InputArray_HS = InputArray.clone();

		/* ALGORITHMS */

		// Part C
		// (i) With the value of S fixed, plot the number of key comparisons over
		// different sizes of the input list n. Compare your empirical results with
		// your theoretical analysis of the time complexity.

		// Fix S at 100
		hybridSort_bySize(InputArray_HS, InputArray.length);


		// (ii) With the input size n fixed, plot the number of key comparisons over
		// different values of S. Compare your empirical results with your
		// theoretical analysis of the time complexity.

		int [] fixedArray = InputArray[2].clone(); // n = 100,000
		// int optimal_S = hybridSort_byS(fixedArray);
		// System.out.printf("The optimal S is %d\n", optimal_S);



		// (iii) Using different sizes of input datasets, study how to determine an
		// optimal value of S for the best performance of this hybrid algorithm.

		insertionSort_bySize(InputArray_IS, InputArray.length);
		// mergeSort_bySize(InputArray_MS, InputArray.length);


		// PART D
		/* TIME COMPLEXITY ANALYSIS */
		// System.out.printf("Time Taken for MergeSort: %d sec\n", (endTime_MS -
		// startTime_MS));
		// System.out.printf("Time Taken for HybridSort: %d sec\n", (endTime_HS -
		// startTime_HS));

	}

	// Generating an array of increasing sizes which contains a randomly generated
	// number //
	public static int[][] generateRandInput(int max) {

		int size = 3, arraySize = 10, step = 10;

		// 10k, 100k, 1mil, 10mil
		int[][] randList = new int[size][];
		Random rand = new Random();

		for (int i = 0; i < size; i++) {
			// Initialize array of n size
			int[] tempArray = new int[arraySize];

			for (int j = 0; j < arraySize; j++) {
				tempArray[j] = rand.nextInt(max);
			}
			randList[i] = tempArray;
			// arraySize += step;
			arraySize *= step;
		}

		return randList;
	}

	// Hybrid Sort for varying array sizes
	public static void hybridSort_bySize(int[][] inputArray, int arraySize){

		System.out.println("\n### HybridSort Algorithm ###\n");
				
		// Save into matrix and create CSV file 
		int[][] inputFile = new int[arraySize][];

		// HYBRIDSORT ALGORITHM //
		for (int i = 0; i < arraySize; i++) {
			int arrayLen = inputArray[i].length;
			int[] resultArray = new int[arraySize];

			resultArray = inputArray[i];

			System.out.println("Input:");
			for(int j=0;j<resultArray.length;j++){
				System.out.printf("%d ", resultArray[j]);
			}
			System.out.println("\n");

			int optimal_S = 100;

			SortingAlgo.resetKeyComparisons();
			long startTime_HS = System.currentTimeMillis();
			SortingAlgo.hybridSort(resultArray, 0, arrayLen-1, optimal_S);
			long endTime_HS = System.currentTimeMillis();
			long keyComp = SortingAlgo.getKeyComparisons();


			
			System.out.println("Sorted:");
			for(int j=0;j<resultArray.length;j++){
				System.out.printf("%d ", resultArray[j]);
			}
			System.out.println("\n");

			// Sanity Check
			// int result = 1;
			// for (int k =1; k<resultArray.length; k++){
			// 	if(!(resultArray[k] >= resultArray[k-1])){
			// 		result = 0;
			// 		System.out.printf("%d, %d", resultArray[k], resultArray[k-1]);
					
			// 	}
			// }
			// if(result==1){
			// 	System.out.println("Correct.");
			// }else{
			// 	System.out.println("Incorrect.");
			// }

			System.out.printf("\nArray of size %d\n", arrayLen);
			System.out.printf("\tTime Taken: %d milliseconds.\n", endTime_HS - startTime_HS);
			System.out.printf("\tNumber of Key Comparisons: %d\n", keyComp);	

			// Save to array then export to CSV
			int[] tempArray = {arrayLen, (int)(endTime_HS - startTime_HS), (int)keyComp};			
			inputFile[i] = tempArray;
		}
		writeToCSV(inputFile, "hybridSort");
	}

	public static void insertionSort_bySize(int[][] inputArray, int arraySize) {

		System.out.println("\n### InsertionSort Algorithm ###\n");
		int[][] inputFile = new int[arraySize][];

		// INSERTIONSORT ALGORITHM //
		for (int i = 0; i < arraySize; i++) {
			int arrayLen = inputArray[i].length;

			long startTime_IS = System.currentTimeMillis();
			SortingAlgo.insertionSort(inputArray[i], arrayLen - 1);
			long endTime_IS = System.currentTimeMillis();
			long keyComp = SortingAlgo.getKeyComparisons();

			System.out.printf("\nArray of size %d\n", arrayLen);
			System.out.printf("\tTime Taken: %d milliseconds.\n", endTime_IS - startTime_IS);
			System.out.printf("\tNumber of Key Comparisons: %d\n", keyComp);

			// Save to array then export to CSV
			int[] tempArray = {arrayLen, (int)(endTime_IS - startTime_IS), (int)keyComp};			
			inputFile[i] = tempArray;
		}
		writeToCSV(inputFile, "insertionSort");	
	}


	public static void mergeSort_bySize(int[][] inputArray, int arraySize) {

		System.out.println("\n### MergeSort Algorithm ###\n");
		int[][] inputFile = new int[arraySize][];

		// MERGESORT ALGORITHM //
		for (int i = 0; i < arraySize; i++) {
			int arrayLen = inputArray[i].length;

			long startTime_MS = System.currentTimeMillis();
			SortingAlgo.mergeSort(inputArray[i], 0, arrayLen - 1);
			long endTime_MS = System.currentTimeMillis();
			long keyComp = SortingAlgo.getKeyComparisons();

			// System.out.printf("\nArray of size %d\n", arrayLen);
			// System.out.printf("\tTime Taken: %d milliseconds.\n", endTime_HS - startTime_HS);
			// System.out.printf("\tNumber of Key Comparisons: %d\n", SortingAlgo.getKeyComparisons());
			
			// Save to array then export to CSV
			int[] tempArray = {arrayLen, (int)(endTime_MS - startTime_MS), (int)keyComp};			
			inputFile[i] = tempArray;
		}
		writeToCSV(inputFile, "mergeSort");	
	}


	// Obtain Optimal S for HybridSort
	public static int hybridSort_byS(int[] inputArray) {
		int start = 0, end = 300, step = 10;
		int optimal_S = start;
		long optimal_keyComp = 999999999;

		int[][] inputFile = new int[400][];

		// Different values of S
		for (int i = start; i < end; i += step) {
			int[] tempInputArray = inputArray.clone();

			SortingAlgo.hybridSort(tempInputArray, 0, tempInputArray.length - 1, i);

			long keyComp = SortingAlgo.getKeyComparisons();

			// Get the optimal S (Lowest key comparisons)
			if (optimal_keyComp > keyComp) {
				optimal_keyComp = keyComp;
				optimal_S = i;
			}

			System.out.printf("S: %d \t Number of Key Comparisons: %d\n", i, keyComp);

			// Save to array then export to CSV
			int[] tempArray = {i, (int)keyComp};
			inputFile[i] = tempArray;
		}

		// writeToCSV(inputFile, "hybridSort_Varying_S");

		return optimal_S;
	}

	public static void writeToCSV(int[][] inputArray, String filename){
		
		try{
			CSVWriter writer = new CSVWriter(new FileWriter("C:\\Users\\eugen\\Desktop\\Coding\\NTU_CODING\\SC2001_Coding\\SC2001_Project1\\Results\\" + filename + ".csv"));

			String [] header = {"ArraySize", "TimeInMs", "KeyComparisons"};
			writer.writeNext(header);
			
			// Write Data
			for(int i=0; i<inputArray.length;i++){
				String[] data = new String[inputArray[i].length];
				for(int j=0; j<inputArray[i].length; j++){
					data[j] = Integer.toString(inputArray[i][j]);
				}
				writer.writeNext(data);
			}
			writer.close();
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}
