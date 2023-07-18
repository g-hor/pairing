// 238. Product of Array Except Self

// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.


var productExceptSelf = function(nums) {
  let length = nums.length;
  let forward = 1;
  let backward = 1;
  const output = new Array(length).fill(1);

  nums.forEach((num, idx) => {
    output[idx] *= forward;
    forward *= num;
  })

  for (let i = length - 1; i >= 0; i--) {
    output[i] *= backward;
    backward *= nums[i];
  }

  return output;
};