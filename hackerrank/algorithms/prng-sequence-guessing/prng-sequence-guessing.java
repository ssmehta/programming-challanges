import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;


public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int N = in.nextInt();
        long startTime, endTime;
        int[] numbers = new int[10], attempts = new int[10];
        
        
        for(int i = 0; i < N; i++) {
            // Read start and end times
            startTime = in.nextLong();
            endTime = in.nextLong();
            
            // Read in known random numbers
            for(int j = 0; j < 10; j++)
                numbers[j] = in.nextInt();
            
            // Loop over all possible seed values
            for(long seed = startTime; seed <= endTime; seed++) {
                Random random = new Random(seed);
                
                // Generate the first ten random numbrs for this seed
                for(int j = 0; j < 10; j++)
                    attempts[j] = random.nextInt(1000);
                
                if(Arrays.equals(attempts, numbers)) {
                    // Print the seed
                    System.out.print(seed);
                    
                    // Generate an print the next ten
                    for(int j = 0; j < 10; j++)
                        System.out.print(" "+ Integer.toString(random.nextInt(1000)));
                    
                    System.out.println();
                    break;
                }
            }
        }
    }
}
