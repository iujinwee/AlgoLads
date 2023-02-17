public class SortingAlgo {

	private static long keycomparison = 0; 

	// PART A 
	// HYBRID SORT ALGORITHM  // 
	public static void hybridSort(int[] inputArray, int start, int end, int S) {

		int mid = (start + end)/2; 
		
		// Insertion Sort
		if(end-start<=0) return;
		else if(end - start <= S){
			insertionSort(inputArray, inputArray.length);
		}
		else if(end - start>1){
			// Merge Sort
			if(end > start) {
				hybridSort(inputArray, start, mid, S);
				hybridSort(inputArray, mid+1, end, S);
				
			}
		}
		
		merge(inputArray, start, end);
	}
	
	
    // MERGE SORT ALGORITHM //
	public static void mergeSort(int[] inputArray, int start, int end) {
		
		int mid = (start + end)/2; 
		
		// Base case  
		if(end > start) {
			mergeSort(inputArray, start, mid);
			mergeSort(inputArray, mid+1, end);
			merge(inputArray, start, end);
		}
		
	}
	
	private static void merge(int[] inputArray, int start, int end) {
        
		int mid = (start + end)/2;
		int a = start, b = mid+1, tmp;
		
		
		if(end > start) {
			while((a <= mid)&&(b<=end)) {
				keycomparison++;
				// Shifting 
				if(inputArray[a] > inputArray[b]) {
					tmp = inputArray[b++];

					for(int i = ++mid; i > a; i--) {
						inputArray[i] = inputArray[i-1]; 
					}
					inputArray[a++] = tmp;
				}
				
				// Continue 
				else if(inputArray[a] < inputArray[b]) {
					a++;
				}
				
				// Same items 
				else { 
					
					// Base case (1 item each subarray)
					if((a == mid ) && (b == end)) {
						break;
					}
					
					tmp = inputArray[b++];
					a++;
					for(int i = ++mid; i > a; i--) {
						inputArray[i] = inputArray[i-1];
					}
					inputArray[a++] = tmp;
				}
			}
		}
		
	}
	

	// INSERTION SORT ALGORITHM //
	public static void insertionSort(int[] inputArray, int size) {
		
		for (int i = 1; i<size; i++) {
			for(int j = i; j > 0; j--) {

				// Count key comparisons
				keycomparison++;

				if(inputArray[j] < inputArray[j-1]) {
					swap(inputArray, j, j-1);
				}else {
					break;
				}
			}
		}
		
	}

	private static void swap(int[] inputArray, int i, int j){	
		int tmp = inputArray[i];
		inputArray[i] = inputArray[j];
		inputArray[j] = tmp;
	}

	public static long getKeyComparisons(){
		long total = keycomparison;
		keycomparison = 0; // Reset key comparisons
		return total;
	}

	public static void resetKeyComparisons(){
		keycomparison = 0;
	}
}
	
	
	
	
