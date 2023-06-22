// 283. Move Zeroes

// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.


var moveZeroes = function(nums) {
  let zeroPos = 0;
  let nonZero = 0;

  for (let i = 0; i < nums.length; i++) {
      if (nums[i] === 0) {
          zeroPos = i;

          while (nums[nonZero] === 0) {
              if (nums[nonZero + 1] === undefined) break;
              nonZero++;
          }

          if (nums[nonZero] !== 0) {
              [nums[zeroPos], nums[nonZero]] = [nums[nonZero], nums[zeroPos]];
              let temp = nonZero;
              zeroPos = temp;
          }
      } 
  }

  return nums;
};