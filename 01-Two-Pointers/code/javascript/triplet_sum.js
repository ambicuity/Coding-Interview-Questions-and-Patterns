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

/**
 * Find all triplets that sum to zero using two-pointer technique.
 * @param {number[]} nums - Array of integers
 * @returns {number[][]} Array of triplets [a, b, c] where a + b + c = 0
 */
function tripletSum(nums) {
    const triplets = [];
    nums.sort((a, b) => a - b);
    
    for (let i = 0; i < nums.length; i++) {
        // Optimization: triplets consisting of only positive numbers will never sum to 0
        if (nums[i] > 0) break;
        
        // To avoid duplicate triplets, skip 'a' if it's the same as the previous number
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        
        // Find all pairs that sum to a target of '-a' ('-nums[i]')
        const pairs = pairSumSortedAllPairs(nums, i + 1, -nums[i]);
        for (const pair of pairs) {
            triplets.push([nums[i], ...pair]);
        }
    }
    
    return triplets;
}

/**
 * Find all pairs in sorted array that sum to target value.
 * @param {number[]} nums - Sorted array of integers
 * @param {number} start - Starting index for the search
 * @param {number} target - Target sum value
 * @returns {number[][]} Array of pairs [b, c] where b + c = target
 */
function pairSumSortedAllPairs(nums, start, target) {
    const pairs = [];
    let left = start, right = nums.length - 1;
    
    while (left < right) {
        const sum = nums[left] + nums[right];
        
        if (sum === target) {
            pairs.push([nums[left], nums[right]]);
            left++;
            
            // To avoid duplicate '[b, c]' pairs, skip 'b' if it's the same as the previous number
            while (left < right && nums[left] === nums[left - 1]) {
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
 * @param {number[]} nums - Array of integers
 * @returns {number[][]} Array of triplets that sum to zero
 */
function tripletSumBruteForce(nums) {
    const n = nums.length;
    const triplets = new Set();
    
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            for (let k = j + 1; k < n; k++) {
                if (nums[i] + nums[j] + nums[k] === 0) {
                    const triplet = [nums[i], nums[j], nums[k]].sort((a, b) => a - b);
                    triplets.add(JSON.stringify(triplet));
                }
            }
        }
    }
    
    return Array.from(triplets).map(triplet => JSON.parse(triplet));
}

/**
 * Test function with comprehensive test cases.
 */
function testTripletSum() {
    console.log("Testing Triplet Sum Solutions");
    console.log("=".repeat(40));
    
    const testCases = [
        {
            input: [0, -1, 2, -3, 1],
            expected: [[-3, 1, 2], [-1, 0, 1]],
            description: 'Basic example'
        },
        {
            input: [],
            expected: [],
            description: 'Empty array'
        },
        {
            input: [0],
            expected: [],
            description: 'Single element'
        },
        {
            input: [1, -1],
            expected: [],
            description: 'Two elements'
        },
        {
            input: [0, 0, 0],
            expected: [[0, 0, 0]],
            description: 'All same values'
        },
        {
            input: [1, 0, 1],
            expected: [],
            description: 'No valid triplets'
        },
        {
            input: [0, 0, 1, -1, 1, -1],
            expected: [[-1, 0, 1]],
            description: 'Duplicate triplets'
        },
        {
            input: [-1, 0, 1, 2, -1, -4],
            expected: [[-1, -1, 2], [-1, 0, 1]],
            description: 'Complex case'
        }
    ];
    
    testCases.forEach((test, index) => {
        // Test optimized solution
        const result = tripletSum([...test.input]);
        const resultSorted = result.map(triplet => [...triplet].sort((a, b) => a - b))
                                   .sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
        const expectedSorted = test.expected.map(triplet => [...triplet].sort((a, b) => a - b))
                                          .sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
        
        const success = JSON.stringify(resultSorted) === JSON.stringify(expectedSorted);
        const status = success ? "✓ PASS" : "✗ FAIL";
        
        console.log(`Test ${index + 1}: ${test.description}`);
        console.log(`Input: [${test.input.join(', ')}]`);
        console.log(`Expected: ${JSON.stringify(test.expected)}`);
        console.log(`Got: ${JSON.stringify(result)}`);
        console.log(`Result: ${status}`);
        
        // Test brute force for comparison (only for small inputs)
        if (test.input.length <= 6) {
            const bruteResult = tripletSumBruteForce([...test.input]);
            const bruteSorted = bruteResult.map(triplet => [...triplet].sort((a, b) => a - b))
                                          .sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
            const bruteMatch = JSON.stringify(bruteSorted) === JSON.stringify(expectedSorted);
            console.log(`Brute force match: ${bruteMatch ? '✓' : '✗'}`);
        }
        
        console.log("-".repeat(40));
    });
}

// Run tests if this file is executed directly
if (typeof require !== 'undefined' && require.main === module) {
    // Run comprehensive tests
    testTripletSum();
    
    // Interactive example
    console.log("\nInteractive Example:");
    const exampleInput = [0, -1, 2, -3, 1];
    console.log(`Input: [${exampleInput.join(', ')}]`);
    const result = tripletSum(exampleInput);
    console.log(`Triplets that sum to zero: ${JSON.stringify(result)}`);
}

// Export functions for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        tripletSum,
        pairSumSortedAllPairs,
        tripletSumBruteForce,
        testTripletSum
    };
}