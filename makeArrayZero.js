// 2357. Make Array Zero by Subtracting Equal Amounts

// You are given a non-negative integer array nums. In one operation, you must:

// Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
// Subtract x from every positive element in nums.
// Return the minimum number of operations to make every element in nums equal to 0.


const minimumOperations = (nums) => {
  let amountOperations = 0;
  let notAllZeroes = nums.some(num => num !== 0);

  while (notAllZeroes) {
      notAllZeroes = false;
      let minimum = nums[0];

      nums.forEach(num => {
          if (minimum === 0 && num !== 0) minimum = num;
          if (num < minimum && num !== 0) minimum = num;
      })

      for (let index = 0; index < nums.length; index++) {
          if (nums[index] !== 0) {
              nums[index] -= minimum;
              notAllZeroes = true;
          }
      }

      if (!notAllZeroes) break;

      amountOperations++;
  }

  return amountOperations;
};