// 817. Linked List Components

// You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

// Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

var numComponents = function(head, nums) {
  let connected = 0;
  let curr = head;
  const numsSet = new Set(nums);

  while (curr) {

      if (numsSet.has(curr.val)) {
          while (curr && numsSet.has(curr.val)) {
              curr = curr.next;
          }

          connected++;
      }

      if (curr) curr = curr.next;
  }


  return connected;
};