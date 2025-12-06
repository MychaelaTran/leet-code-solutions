import java.util.Random;

class Solution {
    //fisher yates

    private int[] og;
    private int[] array; 
    private Random rand = new Random();

    public Solution(int[] nums) {
        og = nums.clone(); 
        array = nums.clone(); 
    }
    
    public int[] reset() {
        array = og.clone(); 
        return array;
    }
    
    public int[] shuffle() {
      for (int i = array.length - 1; i > 0; i--) {
            int rand_index = rand.nextInt(i + 1);  //GET RANDOM INDEX
            //swap array at i and random index 
            int temp = array[i];
            array[i] = array[rand_index];
            array[rand_index] = temp;
        }
        return array;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */