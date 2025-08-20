/**
 * Triplet Sum - Two Pointers Solution
 * Author: Ritesh Rana
 * 
 * Problem: Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0.
 * The solution must not contain duplicate triplets.
 * 
 * Time Complexity: O(n²)
 * Space Complexity: O(n) - not counting output space
 */

import java.util.*;

public class TripletSum {
    
    /**
     * Find all triplets that sum to zero using two-pointer technique.
     * 
     * @param nums Array of integers
     * @return List of triplets [a, b, c] where a + b + c = 0
     */
    public List<List<Integer>> tripletSum(int[] nums) {
        List<List<Integer>> triplets = new ArrayList<>();
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length; i++) {
            // Optimization: triplets consisting of only positive numbers will never sum to 0
            if (nums[i] > 0) break;
            
            // To avoid duplicate triplets, skip 'a' if it's the same as the previous number
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // Find all pairs that sum to a target of '-a' ('-nums[i]')
            List<List<Integer>> pairs = pairSumSortedAllPairs(nums, i + 1, -nums[i]);
            for (List<Integer> pair : pairs) {
                List<Integer> triplet = new ArrayList<>();
                triplet.add(nums[i]);
                triplet.addAll(pair);
                triplets.add(triplet);
            }
        }
        
        return triplets;
    }
    
    /**
     * Find all pairs in sorted array that sum to target value.
     * 
     * @param nums Sorted array of integers
     * @param start Starting index for the search
     * @param target Target sum value
     * @return List of pairs [b, c] where b + c = target
     */
    private List<List<Integer>> pairSumSortedAllPairs(int[] nums, int start, int target) {
        List<List<Integer>> pairs = new ArrayList<>();
        int left = start, right = nums.length - 1;
        
        while (left < right) {
            int sum = nums[left] + nums[right];
            
            if (sum == target) {
                pairs.add(Arrays.asList(nums[left], nums[right]));
                left++;
                
                // To avoid duplicate '[b, c]' pairs, skip 'b' if it's the same as the previous number
                while (left < right && nums[left] == nums[left - 1]) {
                    left++;
                }
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return pairs;
    }
    
    /**
     * Brute force solution for comparison - O(n³) time complexity.
     * 
     * @param nums Array of integers
     * @return List of triplets that sum to zero
     */
    public List<List<Integer>> tripletSumBruteForce(int[] nums) {
        int n = nums.length;
        Set<List<Integer>> triplets = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> triplet = Arrays.asList(nums[i], nums[j], nums[k]);
                        Collections.sort(triplet);
                        triplets.add(triplet);
                    }
                }
            }
        }
        
        return new ArrayList<>(triplets);
    }
    
    /**
     * Test function with comprehensive test cases.
     */
    public void testTripletSum() {
        System.out.println("Testing Triplet Sum Solutions");
        System.out.println("=".repeat(40));
        
        TestCase[] testCases = {
            new TestCase(new int[]{0, -1, 2, -3, 1}, 
                        Arrays.asList(Arrays.asList(-3, 1, 2), Arrays.asList(-1, 0, 1)), 
                        "Basic example"),
            new TestCase(new int[]{}, Arrays.asList(), "Empty array"),
            new TestCase(new int[]{0}, Arrays.asList(), "Single element"),
            new TestCase(new int[]{1, -1}, Arrays.asList(), "Two elements"),
            new TestCase(new int[]{0, 0, 0}, Arrays.asList(Arrays.asList(0, 0, 0)), "All same values"),
            new TestCase(new int[]{1, 0, 1}, Arrays.asList(), "No valid triplets"),
            new TestCase(new int[]{0, 0, 1, -1, 1, -1}, Arrays.asList(Arrays.asList(-1, 0, 1)), "Duplicate triplets"),
            new TestCase(new int[]{-1, 0, 1, 2, -1, -4}, 
                        Arrays.asList(Arrays.asList(-1, -1, 2), Arrays.asList(-1, 0, 1)), 
                        "Complex case")
        };
        
        for (int i = 0; i < testCases.length; i++) {
            TestCase test = testCases[i];
            
            // Test optimized solution
            List<List<Integer>> result = tripletSum(test.input.clone());
            List<List<Integer>> resultSorted = sortTriplets(result);
            List<List<Integer>> expectedSorted = sortTriplets(test.expected);
            
            boolean success = resultSorted.equals(expectedSorted);
            String status = success ? "✓ PASS" : "✗ FAIL";
            
            System.out.println("Test " + (i + 1) + ": " + test.description);
            System.out.println("Input: " + Arrays.toString(test.input));
            System.out.println("Expected: " + test.expected);
            System.out.println("Got: " + result);
            System.out.println("Result: " + status);
            
            // Test brute force for comparison (only for small inputs)
            if (test.input.length <= 6) {
                List<List<Integer>> bruteResult = tripletSumBruteForce(test.input.clone());
                List<List<Integer>> bruteSorted = sortTriplets(bruteResult);
                boolean bruteMatch = bruteSorted.equals(expectedSorted);
                System.out.println("Brute force match: " + (bruteMatch ? "✓" : "✗"));
            }
            
            System.out.println("-".repeat(40));
        }
    }
    
    /**
     * Helper method to sort triplets for comparison.
     */
    private List<List<Integer>> sortTriplets(List<List<Integer>> triplets) {
        List<List<Integer>> sorted = new ArrayList<>();
        for (List<Integer> triplet : triplets) {
            List<Integer> sortedTriplet = new ArrayList<>(triplet);
            Collections.sort(sortedTriplet);
            sorted.add(sortedTriplet);
        }
        sorted.sort((a, b) -> {
            for (int i = 0; i < Math.min(a.size(), b.size()); i++) {
                int comp = a.get(i).compareTo(b.get(i));
                if (comp != 0) return comp;
            }
            return Integer.compare(a.size(), b.size());
        });
        return sorted;
    }
    
    /**
     * Helper class for test cases.
     */
    private static class TestCase {
        int[] input;
        List<List<Integer>> expected;
        String description;
        
        TestCase(int[] input, List<List<Integer>> expected, String description) {
            this.input = input;
            this.expected = expected;
            this.description = description;
        }
    }
    
    /**
     * Main method for running tests and examples.
     */
    public static void main(String[] args) {
        TripletSum solution = new TripletSum();
        
        // Run comprehensive tests
        solution.testTripletSum();
        
        // Interactive example
        System.out.println("\nInteractive Example:");
        int[] exampleInput = {0, -1, 2, -3, 1};
        System.out.println("Input: " + Arrays.toString(exampleInput));
        List<List<Integer>> result = solution.tripletSum(exampleInput);
        System.out.println("Triplets that sum to zero: " + result);
    }
}